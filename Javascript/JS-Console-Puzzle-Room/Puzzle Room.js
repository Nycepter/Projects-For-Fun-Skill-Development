console.log(
  "You wake up in an unfamiliar room. There is a TV, a door, and a desk."
);
while (true) {
  let rlSync = require("readline-sync");
  let choice1 = rlSync.question(
    "Do you investigate the 'TV', the 'Door', or the 'Desk'?\n"
  );
  if (choice1 == "Quit") {
    return;
  } else if (choice1 == "TV") {
    console.log("The TV is currently off.");
    let rlSync = require("readline-sync");
    let choice2 = rlSync.question("Do you 'Turn the TV on' or 'Go back'?\n");

    if (choice2 == "Turn the TV on") {
      console.log(
        "A hissing noise immentates from the TV as static erupts on the screen, slowly a picture comes into view, the number 13 flashes on the screen. All other channels are static, What would you like to do next?"
      );
      continue;
    } else if (choice2 == "Go back") {
      continue;
    }
  } else if (choice1 == "Door") {
    console.log(
      "The door is locked by a dgital lock that allows the input of three single digit numbers."
    );
    let rlSync = require("readline-sync");
    let choice3 = rlSync.question("Do you 'Input code' or 'Go back'?\n");
    if (choice3 == "Input code") {
      let number1 = Number(rlSync.question("Enter the first number\n"));
      let number2 = Number(rlSync.question("Enter the second number\n"));
      let number3 = Number(rlSync.question("Enter the second number\n"));
      let sum = number1 + number2 + number3;
      if (sum == 20) {
        console.log("You hear a click as the door is unlocked!");
        let rlSync = require("readline-sync");
        let choice5 = rlSync.question("Do you want to go through the door?\n");
        if (choice5 == "Yes") {
          console.log(
            "You push the door open, as you walk through you descover.... That you will have to wait for Chapter 2 ;)  THANK YOU FOR PLAYING"
          );
          return;
        } else if (choice5 == "No") {
          continue;
        }
      }
    } else {
      console.log(
        "The lock flashes red, the combination you entered was incorrect."
      );
      continue;
    }
    if (choice3 == "Go back") {
      continue;
    }
  } else if (choice1 == "Desk") {
    console.log("The desk two drawers");
    let rlSync = require("readline-sync");
    let choice6 = rlSync.question(
      "Do you want to 'Open the top drawer', 'Open the bottom drawer', or 'Go Back?\n"
    );
    if (choice6 == "Open the top drawer") {
      console.log("The top drawer slides open to reveal that it is empty.");
      let rlSync = require("readline-sync");
      let choice7 = rlSync.question(
        "Do you want to 'Open the bottom drawer', or 'Go Back?\n"
      );
      if (choice7 == "Open the bottom drawer") {
        console.log(
          'You find a piece of paper that says "The world has many wonders!" There is nothing more at the desk.'
        );
        continue;
      } else if (choice7 == "Go back") {
        continue;
      }
    } else if (choice6 == "Open the bottom drawer") {
      console.log(
        'You find a piece of paper that says "The world has many wonders!" There is nothing more at the desk, what would you like to do next?'
      );
      let rlSync = require("readline-sync");
      let choice8 = rlSync.question(
        "Do you want to 'Open the top drawer', or 'Go Back?\n"
      );
      if (choice8 == "Open the top drawer") {
        console.log(
          "The top drawer slides open to reveal that it is empty. There is nothing more at the desk, what would you like to do next?"
        );
        continue;
      } else if (choice8 == "Go back") {
        continue;
      }
    } else if (choice6 == "Go Back") {
      continue;
    }
  }
}
