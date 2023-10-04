let Party = {
  Jacob: {
    name: "Jacob",
    class: "Warlock",
    level: 5,
    healthPoints: 30,
    damage: Math.round(Math.random() * 3),
  },
  Robbie: {
    name: "Robbie",
    class: "Rogue",
    level: 5,
    healthPoints: 45,
    damage: Math.round(Math.random() * 5),
  },
  Grease: {
    name: "Grease",
    class: "Blood Hunter",
    level: 5,
    healthPoints: 40,
    damage: Math.round(Math.random() * 4),
  },
};

let Monsters = {
  Slime: {
    name: "Slime",
    level: 2,
    healthPoints: 15,
    damage: Math.round(Math.random() * 2),
  },
  Dragon: {
    name: "Dragon",
    level: 7,
    healthPoints: 100,
    damage: Math.round(Math.random() * 5),
  },
  Elemental: {
    name: "Elemental",
    level: 4,
    healthPoints: 20,
    damage: Math.round(Math.random() * 4),
  },
  Bandit: {
    name: "Bandit",
    level: 1,
    healthPoints: 10,
    damage: Math.round(Math.random() * 2),
  },
  Zombie: {
    name: "Zombie",
    level: 3,
    healthPoints: 20,
    damage: Math.round(Math.random() * 3),
  },
};

let AdventureText = [
  "You must stop a dragon that has been attacking nearby villages.",
  "You have to destroy a slime and  a zombie that have teamed up.",
  "A bandit has summoned an elemental and has been killing guards, you must stop them.",
];

let dragonAdv = AdventureText[0];
let slimZomAdv = AdventureText[1];
let elemBandAdv = AdventureText[2];

let AdventureGroup = [dragonAdv]; //, slimZomAdv, elemBandAdv];ADD THESE BACK!!!!!!!

AdventureRef =
  AdventureGroup[Math.floor(Math.random() * AdventureGroup.length)];

Party.Jacob.damage = Party.Jacob.damage * Party.Jacob.level;
Party.Robbie.damage = Party.Robbie.damage * Party.Robbie.level;
Party.Grease.damage = Party.Grease.damage * Party.Grease.level;
Monsters.Slime.damage = Monsters.Slime.damage * Monsters.Slime.level;
Monsters.Bandit.damage = Monsters.Bandit.damage * Monsters.Bandit.level;
Monsters.Dragon.damage = Monsters.Dragon.damage * Monsters.Dragon.level;
Monsters.Elemental.damage =
  Monsters.Elemental.damage * Monsters.Elemental.level;
Monsters.Zombie.damage = Monsters.Zombie.damage * Monsters.Zombie.level;

let monster = "";
let monster1 = "";
let monster2 = "";

function getAdventure() {
  return AdventureRef;
}

console.log(AdventureText[0]);

if (getAdventure() == AdventureText[0]) {
  console.log("You enter combat with the dragon!");
} else if (getAdventure() == AdventureText[1]) {
  console.log("You enter combat with a slime and zombie who have teamed up!");
} else if (getAdventure() == AdventureText[2]) {
  console.log("You enter combat with a bandit and his summoned elemental");
} else {
  return;
}

if (getAdventure() == AdventureText[0]) {
  monster = Monsters.Dragon.name;
} else if (getAdventure() == AdventureText[1]) {
  monster1 = Monsters.Slime.name;
  monster2 = Monsters.Zombie.name;
} else if (getAdventure() == AdventureText[2]) {
  monster1 = Monsters.Bandit.name;
  monster2 = Monsters.Elemental.name;
} else {
  return;
}
let mem1 = Party.Robbie;
let mem2 = Party.Jacob;
let mem3 = Party.Grease;

partySela = [mem1, mem2, mem3];
partySel = partySela[Math.floor(Math.random() * partySela.length)];
function partyCombatDamage() {
  if (partySel == mem1) {
    return Party.Robbie.damage;
  } else if (partySel == mem2) {
    return Party.Jacob.damage;
  } else if (partySel == mem3) {
    return Party.Grease.damage;
  }
}

function singleCombat() {
  if ((AdventureRef = AdventureText[0]))
    do {
      console.log(
        `${
          partySel.name
        } attacks the dragon for ${partyCombatDamage()} reducing its HP to ${(Monsters.Dragon.healthPoints =
          Monsters.Dragon.healthPoints - partyCombatDamage())}`
      );

      console.log(
        `The dragon attacks ${partySel.name} for ${
          Monsters.Dragon.damage
        } reducing their HP to ${(partySel.healthPoints =
          partySel.healthPoints - Monsters.Dragon.damage)}`
      );
    } while (Monsters.Dragon.healthPoints > 0 && partySel.healthPoints > 0);
  if (partySel.healthPoints < 1) {
    console.log(`${partySel.name} is dead.`);
  }
}

AdventureRef = AdventureText[0];

function groupCombat() {
  if ((AdventureRef = AdventureText[0]))
    if (Party.Robbie.healthPoints < 1) {
      partySela = [mem2, mem3];
    }
  if (Party.Jacob.healthPoints < 1) {
    partySela = [mem1, mem3];
  }
  if (Party.Grease.healthPoints < 1) {
    partySela = [mem2, mem1];
  }
  if (Party.Robbie.healthPoints < 1 && Party.Jacob.healthPoints < 1) {
    partySela = [mem3];
  }
  if (Party.Robbie.healthPoints < 1 && Party.Grease.healthPoints < 1) {
    partySela = [mem2];
  }
  if (Party.Grease.healthPoints < 1 && Party.Jacob.healthPoints < 1) {
    partySela = [mem1];
  }
  if (
    Party.Robbie.healthPoints < 1 &&
    Party.Grease.healthPoints < 1 &&
    Party.Jacob.healthPoints < 1
  ) {
    console.log("The party was defeated by the dragon...");
    return;
  }
  if (Monsters.Dragon.healthPoints < 1) {
    console.log(`The ${Monsters.Dragon.name} is dead!`);
    return;
  }

  do {
    Party.Jacob.damage = Math.round(Math.random() * 3);

    Party.Robbie.damage = Math.round(Math.random() * 5);

    Party.Grease.damage = Math.round(Math.random() * 4);

    Party.Jacob.damage = Party.Jacob.damage * Party.Jacob.level;
    Party.Robbie.damage = Party.Robbie.damage * Party.Robbie.level;
    Party.Grease.damage = Party.Grease.damage * Party.Grease.level;

    Monsters.Dragon.damage = Math.round(Math.random() * 5);
    Monsters.Dragon.damage = Monsters.Dragon.damage * Monsters.Dragon.level;

    if (Party.Robbie.healthPoints < 1) {
      partySela = [mem2, mem3];
    }
    if (Party.Jacob.healthPoints < 1) {
      partySela = [mem1, mem3];
    }
    if (Party.Grease.healthPoints < 1) {
      partySela = [mem2, mem1];
    }
    if (Party.Robbie.healthPoints < 1 && Party.Jacob.healthPoints < 1) {
      partySela = [mem3];
    }
    if (Party.Robbie.healthPoints < 1 && Party.Grease.healthPoints < 1) {
      partySela = [mem2];
    }
    if (Party.Grease.healthPoints < 1 && Party.Jacob.healthPoints < 1) {
      partySela = [mem1];
    }
    if (
      Party.Robbie.healthPoints < 1 &&
      Party.Grease.healthPoints < 1 &&
      Party.Jacob.healthPoints < 1
    ) {
      console.log("The party was defeated by the dragon...");
      return;
    }
    if (Monsters.Dragon.healthPoints < 1) {
      console.log(`The ${Monsters.Dragon.name} is dead!`);
      return;
    }
    partySel = partySela[Math.floor(Math.random() * partySela.length)];

    console.log(
      `${partySel.name} attacks the dragon for ${
        partySel.damage
      } reducing its HP to ${(Monsters.Dragon.healthPoints =
        Monsters.Dragon.healthPoints - partySel.damage)}`
    );

    if (Party.Robbie.healthPoints < 1) {
      partySela = [mem2, mem3];
    }
    if (Party.Jacob.healthPoints < 1) {
      partySela = [mem1, mem3];
    }
    if (Party.Grease.healthPoints < 1) {
      partySela = [mem2, mem1];
    }
    if (Party.Robbie.healthPoints < 1 && Party.Jacob.healthPoints < 1) {
      partySela = [mem3];
    }
    if (Party.Robbie.healthPoints < 1 && Party.Grease.healthPoints < 1) {
      partySela = [mem2];
    }
    if (Party.Grease.healthPoints < 1 && Party.Jacob.healthPoints < 1) {
      partySela = [mem1];
    }
    if (
      Party.Robbie.healthPoints < 1 &&
      Party.Grease.healthPoints < 1 &&
      Party.Jacob.healthPoints < 1
    ) {
      console.log("The party was defeated by the dragon...");
      return;
    }
    if (Monsters.Dragon.healthPoints < 1) {
      console.log(`The ${Monsters.Dragon.name} is dead!`);
      return;
    }
    partySel = partySela[Math.floor(Math.random() * partySela.length)];

    console.log(
      `The dragon attacks ${partySel.name} for ${
        Monsters.Dragon.damage
      } reducing their HP to ${(partySel.healthPoints =
        partySel.healthPoints - Monsters.Dragon.damage)}`
    );

    if (
      Party.Robbie.healthPoints < 1 &&
      Party.Grease.healthPoints < 1 &&
      Party.Jacob.healthPoints < 1
    ) {
      console.log("The party was defeated by the dragon...");
      return;
    }
    if (Monsters.Dragon.healthPoints < 1) {
      console.log(`The ${Monsters.Dragon.name} is dead!`);
      return;
    }
  } while (
    Monsters.Dragon.healthPoints > 0 ||
    (Party.Robbie.healthPoints > 0 &&
      Party.Grease.healthPoints > 0 &&
      Party.Jacob.healthPoints > 0)
  );
}
if (Party.Robbie.healthPoints < 1) {
  console.log(`${Party.Robbie.name} is dead.`);
}

if (Party.Grease.healthPoints < 1) {
  console.log(`${Party.Grease.name} is dead.`);
}

if (Party.Jacob.healthPoints < 1) {
  console.log(`${Party.Jacob.name} is dead.`);

  if (Monsters.Dragon.healthPoints < 1) {
    console.log(`The ${Monsters.Dragon.name} is dead!`);
  }
  if (Monsters.Dragon.healthPoints < 1) {
    console.log("The party was defeated by the dragon...");
    return;
  }
}

groupCombat();
