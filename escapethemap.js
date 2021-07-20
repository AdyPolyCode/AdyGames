const prompt = require('prompt-sync')({sigint: true});

const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';

class Field {
  constructor(array){
    this.array = array;
    this.reset = array.map((subArray) => {
      return subArray.slice();
    });
  }

  printField(){
    let string = '';

    for (let row in this.array){
      if (row !== this.array.length){
        string += (this.array[row].join(' ') + '\n');
      }else{
        string += this.array[row].join(' ')
      };
    };
    return string;
  }

  validateSpot(row, col){
      if (row < 0 || row > this.array.length){
          return false;
      };
      const valid = this.array[row][col];

      if (valid === undefined){
          return false;
      };

      if (String(valid) === 'O' || valid === '*'){
          return false;
      };
      return true;
  }

  reBuild(){
      this.array = this.reset;
  }

  playAgain(){
      let res = prompt('Do you want to play again? ').toLowerCase();

      if (res === 'y'){
          this.reBuild();
          return this.play();
      }else if (res === 'n'){
          return;
      }else{
        this.playAgain();
      };
  }

  play(){
      console.log('Enter u: Up, d: Down, r: Right, l: Left to move on the map.');
      let currentCol = 0;
      let currentRow = 0;
      let done;

      while (!(done)){
        let valid = this.validateSpot(currentRow, currentCol);
        if (valid === false && currentCol !== 0){
            done = false;
            break;
        };
        if (this.array[currentRow][currentCol] === '^'){
          this.array[currentRow][currentCol] = '*';
          done = true;
          break;
        };
        this.array[currentRow][currentCol] = '*';

        console.log(this.printField());

        let userGuess = prompt('Which way? ');
        userGuess = String(userGuess).toLowerCase();

        if (userGuess === 'r'){
            currentCol += 1;
        };
        if (userGuess === 'l'){
            currentCol -= 1
        };
        if (userGuess === 'u'){
            currentRow -= 1;
        };
        if (userGuess === 'd'){
            currentRow += 1;
        };
      };

      if (!(done)){
          console.log('You have lost the game!');
          this.playAgain();
      }else{
        console.log('You have won the game!');
        this.playAgain();
      };
  }
}

const myField = new Field([
  ['*', '░', 'O', '░', '░'],
  ['░', 'O', '░', 'O', '░'],
  ['░', '░', '░', '░', '^'],
  ['░', '░', '░', '░', '░']
]);

myField.play()