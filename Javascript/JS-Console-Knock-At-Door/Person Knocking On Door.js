const Robbie = {
    rfirstName: 'Glenn',
    rmiddleName: 'Robert',
    rlastName: 'McCartney',
    rage: 27,
    rhobbies: ['sucking dick.', 'playing magic.', 'playing Apex Legends.'],
    raddress: {
        street: '1300 S Example St',
        city: 'Sheldon',
        State: 'Missouri'
    }
}
const Jacob = {
    jfirstName: 'Jacob',
    jmiddleName: 'dale',
    jlastName: 'McCartney',
    jage: 24,
    jhobbies: ['riding men.', 'playing basketball.', 'playing Dungeons and Dragons.'],
    jaddress: {
        street: '1301 S Example St',
        city: 'Sheldon',
        State: 'Missouri'
    }   
}
const {rfirstName, rmiddleName, rlastName, rage, rhobbies, raddress} = Robbie;
const {jfirstName, jmiddleName, jlastName, jage, jhobbies, jaddress} = Jacob;

let knockAtDoor = true
let personKnocking = [Robbie, Jacob]

personKnocking = personKnocking[Math.floor(Math.random()*personKnocking.length)];

if (knockAtDoor) {
    if (personKnocking === Robbie) {
        console.log(`Hello ${Robbie.rfirstName}, I heard you like ${Robbie.rhobbies[Math.floor(Math.random()*Robbie.rhobbies.length)]}`);
    } else if (personKnocking === Jacob) {
        console.log(`Hello ${Jacob.jfirstName}, I heard you like ${Jacob.jhobbies[Math.floor(Math.random()*Jacob.jhobbies.length)]}`);
    } else {
        console.log('error');
    }
}    