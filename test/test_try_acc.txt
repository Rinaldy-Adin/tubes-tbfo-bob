try {
  let x = 5;
  while(x != 0) {
    console.log(x);
    x--;
  }

  if(false) {
    throw "Hello";
  }

  delete x;
} catch(err) {
  console.log(err);
} finally {
  y += 3;
}