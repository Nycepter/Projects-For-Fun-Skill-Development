const Jacob = {
  Name: "Jacob",
  age: 24,
  gender: "Boy",
};
const Robbie = {
  Name: "Robbie",
  age: 28,
  gender: "Boy",
};
const Alex = {
  Name: "Alex",
  age: 30,
  gender: "Boy",
};
const Rick = {
  Name: "Rick",
  age: 14,
  gender: "Boy",
};
const Larry = {
  Name: "Larry",
  age: 24,
  gender: "Boy",
};
const Sarah = {
  Name: "Sarah",
  age: 13,
  gender: "Girl",
};
const Amber = {
  Name: "Amber",
  age: 27,
  gender: "Girl",
};
const Chelsey = {
  Name: "Chelsey",
  age: 22,
  gender: "Girl",
};
const Emma = {
  Name: "Emma",
  age: 19,
  gender: "Girl",
};
const Betty = {
  Name: "Betty",
  age: 29,
  gender: "Girl",
};

let People = [
  Jacob,
  Rick,
  Robbie,
  Alex,
  Larry,
  Sarah,
  Amber,
  Chelsey,
  Emma,
  Betty,
];

let Partner1 = People[Math.floor(Math.random() * People.length)];
let Partner2 = People[Math.floor(Math.random() * People.length)];

do {
  Partner2 = People[Math.floor(Math.random() * People.length)];
} while (Partner2.Name == Partner1.Name);

if (Partner1.gender === Partner2.gender) {
  console.log(
    `${Partner1.Name} and ${Partner2.Name} cannot have a child because they are the same gender. `
  );
  return;
} else {
  console.log(`${Partner1.Name} and ${Partner2.Name} can have a child. `);
}

if (Partner1.age < 18 || Partner2.age < 18) {
  console.log("However, at least one of them is underage and that is illegal.");
} else {
  console.log("And they will!");
}
