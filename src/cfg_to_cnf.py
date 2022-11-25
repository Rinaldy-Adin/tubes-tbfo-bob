import json, os


def cfgtxt_to_dict(filepath: str):
    f = open(filepath, "r")
    cfg_string = f.read()
    cfg_list = cfg_string.splitlines()

    cfg_dict = {}
    for production_string in cfg_list:
        prod_left = production_string.split("->")[0]
        prod_right = production_string.split("->")[1]

        prod_left = prod_left.lstrip().rstrip()
        prod_rules = prod_right.split(" | ")
        cfg_dict[prod_left] = []
        for rule in prod_rules:
            rule = rule.lstrip().rstrip()
            rule_result_list = rule.split()
            cfg_dict[prod_left].append(rule_result_list)

    return cfg_dict


def remove_nullables(rules: list[list[str]], nullables: list[str]):
    i = 0
    while i < len(rules):
        rule = rules[i]
        for idx, symbol in enumerate(rule):
            if symbol in nullables:
                # rule without nullable
                tmp_rule = rule.copy()
                del tmp_rule[idx]

                if tmp_rule and tmp_rule not in rules:
                    rules.append(tmp_rule)
        i += 1

    return rules


def isTerminal(str):
    for c in str:
        if c >= "A" and c <= "Z":
            return False
    return True


def cfg_to_cnf(filepath: str):
    cfg_dict = cfgtxt_to_dict(filepath)

    # REMOVE EPSILON PRODUCTIONS
    nullables = []

    # Add nullable variables into list
    for prod_src in cfg_dict:
        tmp_rules = []
        rules = cfg_dict[prod_src]
        for idx, rule in enumerate(rules):
            if "@epsilon" in rule:
                nullables.append(prod_src)
            else:
                tmp_rules.append(rule)
        rules[:] = tmp_rules

    # Remove nullable productions
    for prod_src in cfg_dict:
        cfg_dict[prod_src] = remove_nullables(cfg_dict[prod_src], nullables)

    # REMOVE UNIT PRODUCTIONS
    # Add zero step unit pairs to dict
    unit_pairs = {}
    for prod_src in cfg_dict:
        unit_pairs[prod_src] = [prod_src]


    # Add other unit pairs to dict
    # and remove unit productions from CFG
    for prod_src in unit_pairs:
        i = 0
        while i < len(unit_pairs[prod_src]):
            prod_pair = unit_pairs[prod_src][i]
            rules = cfg_dict[prod_pair]
            for rule in rules:
                if len(rule) == 1 and not isTerminal(rule[0]):
                    if rule[0] not in unit_pairs[prod_src]:
                        unit_pairs[prod_src].append(rule[0])
            i += 1

    for prod_src in cfg_dict:
      tmp_rules = []
      rules = cfg_dict[prod_pair]
      for rule in rules:
        if not (len(rule) == 1 and not isTerminal(rule[0])):
          tmp_rules.append(rule)
      rules[:] = tmp_rules

    # Add productions to CFG based off unit pairs
    unit_eliminated = cfg_dict.copy()
    for prod_src in unit_pairs:
        for prod_pair in unit_pairs[prod_src]:
            src_rules = cfg_dict[prod_src]
            pair_rules = unit_eliminated[prod_pair]
            for rule in pair_rules:
                if rule not in src_rules:
                    src_rules.append(rule)

    # print(json.dumps(unit_pairs, indent=4))
    # print(json.dumps(unit_eliminated, indent=4))

    
    # for key, value in cfg_dict.items():
    #   print(key, ":", value)
    
    # print("\n\n\n\n")

    # TURN PRODUCTIONS OF LENGTH 2
    # OR MORE TO VARIABLE ONLY
    term_to_var_mapping = {}
    unused_term_num = 0

    # Map terminals to variables
    for prod_src in cfg_dict:
        for rule in cfg_dict[prod_src]:
            for idx, symbol in enumerate(rule):
                if len(rule) >= 2 and isTerminal(symbol):
                    if symbol not in term_to_var_mapping:
                        unused_term_num += 1
                        varname = "TER-" + symbol.upper()
                        term_to_var_mapping[symbol] = varname
                    rule[idx] = term_to_var_mapping[symbol]


    # Add variable productions to CFG
    for term in term_to_var_mapping:
        varname = term_to_var_mapping[term]
        cfg_dict[varname] = [[term]]

    # BREAK PRODUCTIONS OF LENGTH 3 OR MORE
    unused_newvar_num = 0
    newvars = {}
    for prod_src in cfg_dict:
        for rule in cfg_dict[prod_src]:
            if len(rule) > 2:
                idx = len(rule) - 2
                newvar = [rule[idx], rule[idx + 1]]
                unused_newvar_num += 1
                newvar_name = "NEWVAR" + str(unused_newvar_num) + "-" + rule[idx]
                newvars[newvar_name] = newvar

                for sym_idx in range(idx - 1, 0, -1):
                    newvar = [rule[sym_idx], newvar_name]
                    unused_newvar_num += 1
                    newvar_name = "NEWVAR" + str(unused_newvar_num) + "-" + rule[sym_idx]
                    newvars[newvar_name] = newvar

                rule[:] = [rule[0], newvar_name]

    # Add new variables to dict
    for newvar in newvars:
        cfg_dict[newvar] = [newvars[newvar]]

    # RETURNS a CNF
    return cfg_dict


# Only for debugging
# if __name__ == "__main__":
#     cfg_path = os.path.join(
#         os.path.dirname(os.path.dirname(__file__)), r"config\testcfg.txt"
#     )
#     cnf = cfg_to_cnf(cfg_path)

#     print(json.dumps(cnf, indent=4))
