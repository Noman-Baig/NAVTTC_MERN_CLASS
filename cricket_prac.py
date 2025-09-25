
const prompt = require("prompt-sync")();

let total_players = 10;

let total_balls_a = 26;
let total_balls_b = 26;

let runsA = 0;
let runsB = 0;

let wicketsA = 0;
let wicketsB = 0;

console.log("\n===== Match Start (TEAM A) ======\n");

for (let i = 0; i < total_balls_a; i++) {
  let shot = prompt(
    `\nBall > ${total_balls_a} | Runs ${runsA}/ Outs ${wicketsA} Player${
      wicketsA + 1
    } : `
  );

  if (!shot) {
    console.log("Press O/Out for out || 1-6 for Runs");
  } else if (shot.toLowerCase() === "out" || shot.toLowerCase() === "o") {
    total_balls_a -= 1;
    wicketsA += 1;
    if (wicketsA === total_players) {
      console.log(`\nAll Players out | Total Score ${runsA}\n`);
      wicketsA = 0;
      break;
    }
  } else {
    let run = parseInt(shot);
    if (isNaN(run) || run > 6 || run < 0) {
      console.log("Only 0-6 Runs Allowed");
    } else {
      total_balls_a -= 1;
      runsA += run;
    }
  }
}

console.log("\n===== Match Start (TEAM B) ======\n");

for (let i = 0; i < total_balls_b; i++) {
  let shot = prompt(
    `\nBall > ${total_balls_b} | Runs ${runsB}/ Outs ${wicketsB} Player${
      wicketsB + 1
    } : `
  );

  if (!shot) {
    console.log("Press O/Out for out || 1-6 for Runs");
  } else if (shot.toLowerCase() === "out" || shot.toLowerCase() === "o") {
    total_balls_b -= 1;
    wicketsB += 1;
    if (wicketsB === total_players) {
      console.log(`\nAll Players out | Total Score ${runsB}\n`);
      wicketsB = 0;
      break;
    }
  } else {
    let run = parseInt(shot);
    if (isNaN(run) || run > 6 || run < 0) {
      console.log("Only 0-6 Runs Allowed");
    } else {
      total_balls_b -= 1;
      runsB += run;
    }
  }
}

if (runsA > runsB) {
  console.log(`\nTeam A Win the Match || Total Runs ${runsA}!`);
} else if (runsB > runsA) {
  console.log(`\nTeam B Win the Match || Total Runs ${runsB}!`);
} else {
  console.log("\nDraw hogaya bhai !");
}
