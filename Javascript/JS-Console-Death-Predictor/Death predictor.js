const date1 = {
  Month: [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ],
  Day: "",
  Year: Math.floor(Math.random() * 3000),
};

let deathMethod1 = [
  "by being stabbed to death by a crackhead.",
  "when you aciddentally fell down a manhole.",
  "from falling out of bed and hitting your head.",
  "by drowning in a barrel of mead.",
  "from being eaten by a badger.",
  "from being shot in the head by Rick, from down the street.",
  "by overdosing on heroin that you got from Demi Lovato.",
  "when you choke on a Carrot.",
  'from attempting to break the "Tide-Pod challenge" world record.',
  "when actual cannibal Shia LaBeouf hunts you through the woods.",
  "when Butcher Pete comes hackin, and wackin, and smackin.",
];

deathMethod1 = deathMethod1[Math.floor(Math.random() * deathMethod1.length)];
date1.Month = date1.Month[Math.floor(Math.random() * date1.Month.length)];

if (date1.Month == "February") {
  date1.Day = Math.floor(Math.random() * 28) + 1;
} else if (date1.Month == "April") {
  date1.Day = Math.floor(Math.random() * 30) + 1;
} else if (date1.Month == "June") {
  date1.Day = Math.floor(Math.random() * 30) + 1;
} else if (date1.Month == "September") {
  date1.Day = Math.floor(Math.random() * 30) + 1;
} else if (date1.Month == "November") {
  date1.Day = Math.floor(Math.random() * 30) + 1;
} else if (date1.Month == "January") {
  date1.Day = Math.floor(Math.random() * 31) + 1;
} else if (date1.Month == "March") {
  date1.Day = Math.floor(Math.random() * 31) + 1;
} else if (date1.Month == "May") {
  date1.Day = Math.floor(Math.random() * 31) + 1;
} else if (date1.Month == "July") {
  date1.Day = Math.floor(Math.random() * 31) + 1;
} else if (date1.Month == "August") {
  date1.Day = Math.floor(Math.random() * 31) + 1;
} else if (date1.Month == "October") {
  date1.Day = Math.floor(Math.random() * 31) + 1;
} else {
  date1.Day = Math.floor(Math.random() * 31) + 1;
}
do {
  date1.Year = Math.floor(Math.random() * 3000);
} while (date1.Year < 2022 || date1.Year > 2099);

function predictDeathDate() {
  console.log(
    `You will die on ${date1.Month} ${date1.Day}, ${date1.Year}. You will die ${deathMethod1}`
  );
}

predictDeathDate();
