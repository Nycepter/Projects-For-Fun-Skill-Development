const Vorinclex = {
    name: 'Vorinclex, Voice of Hunger',
    cost: [2, 6],
    costType: ['Green', 'Colorless'],
    type: ['Legendary', 'Creature', 'Praetor'],
    modifiers: 'Trample',
    effects: "Whenever you tap a land for mana, add one mana to your mana pool of any type that land produced. / Whenever an opponent taps a land for mana, that land doesn't untap during its controller's next untap step.",
    power: 7,
    toughness:6,
}
  
const Psychatog = {
    name: 'Psychatog',
    cost: [1, 1, 1],
    costType: ['Black', 'Blue', 'Colorless'],
    type: ['Creature', 'PraetorAtog'],
    modifiers: null,
    effects: "Discard a card from your hand: Psychatog gets +1/+1 until end of turn. / Remove two cards from the game: Psychatog gets +1/+1 until end of turn.",
    power: 1,
    toughness:2,
}



function murder(target){
    if ((target.type.includes('Creature')) && !(target.modifiers.includes('Indestructable'))) {
        console.log(`${target.name} was destroyed and sent to the graveyard.`);
    } else {
        console.log(`${target.name} cannot be destroyed.`)
    }
}

function castDown(target){
    if (!(target.type.includes('Legendary')) && !(target.modifiers.includes('Indestructable')) && (target.type.includes('Creature'))) {
        console.log(`${target.name} was destroyed and sent to the graveyard.`);
    } else if (target.type.includes('Legendary')) {
        console.log(`${target.name} cannot be destroyed by Cast Down because it is a legendary creature.`) 
    } else {
        console.log(`${target.name} cannot be destroyed.`)
    }
}


