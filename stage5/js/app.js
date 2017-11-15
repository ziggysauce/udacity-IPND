/* JS File */

/*
 * set up the event listener for a card. If a card is clicked:
 * display the card's symbol (put this functionality in another function that you call from this one)
 * add the card to a *list* of "open" cards (put this functionality in another function that you call from this one)
 * if the list already has another card, check to see if the two cards match
 * if the cards do match, lock the cards in the open position (put this functionality in another function that you call from this one)
 * if the cards do not match, remove the cards from the list and hide the card's symbol (put this functionality in another function that you call from this one)
 * increment the move counter and display it on the page (put this functionality in another function that you call from this one)
 * if all cards have matched, display a message with the final score (put this functionality in another function that you call from this one)
 */

const array = ['fa-facebook', 'fa-google-plus', 'fa-instagram', 'fa-pinterest', 'fa-tumblr', 'fa-reddit-alien', 'fa-snapchat-ghost', 'fa-twitter', 'fa-facebook', 'fa-google-plus', 'fa-instagram', 'fa-pinterest', 'fa-tumblr', 'fa-reddit-alien', 'fa-snapchat-ghost', 'fa-twitter'];
const cardId = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16];
const cardContainer = document.getElementsByClassName('deck');
const addMinutes = document.getElementById('minutes');
const addTens = document.getElementById('tensplace');
const addOnes = document.getElementById('onesplace');
let currentPair = [];
let storeId = [];
let storeFirstClick = [];
let clickNum = 0;
let pairs = 0;
let totalClick = 0;
let currentTime = '';
let minutes = 0;
let tens = 0;
let ones = 0;


// Shuffles cards and store values in array
function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }
  return array;
}

/*
 * Display the cards on the page
 *   - shuffle the list of cards using the provided "shuffle" method below
 *   - loop through each card and create its HTML
 *   - add each card's HTML to the page
 *
 * Creates an unordered list (deck)
 * Creates list items within the unordered last (cards)
 * Shows an arrangement of the cards face down
 * Cards are randomized based on shuffle function
 */
function dealCards() {
  let incnum = 1;
  const getDeck = document.getElementById('cont');
  const makeDeck = document.createElement('ul');
  makeDeck.className = 'deck';
  getDeck.appendChild(makeDeck);

  array.map((j) => {
    const createCard = document.createElement('li');
    createCard.className = 'card ';
    createCard.setAttribute('id', `card${incnum}`);
    const createIcon = document.createElement('i');
    createIcon.className = `fa ${j}`;
    incnum += 1;
    createCard.appendChild(createIcon);
    makeDeck.appendChild(createCard);
    return j;
  });
}

/*
 * Show specifically how many moves the user made
 * Show star rating that corresponds to number of moves
 * Show time the user took to complete the game (minutes:seconds:milliseconds)
 */
function scoreKeeper() {
  const getStars = document.getElementById('endstars');
  const getMoves = document.getElementById('finalmoves');
  const getFinalTimes = document.getElementById('finaltime');

  getMoves.append(`${(totalClick / 2).toString()}`);
  getFinalTimes.append(`${addMinutes.innerHTML}:${addTens.innerHTML}:${addOnes.innerHTML}`);

  if (totalClick <= 28) {
    const threeStars = `
    <li><i class="fa fa-star"></i></li>
    <li><i class="fa fa-star"></i></li>
    <li><i class="fa fa-star"></i></li>
    `;
    getStars.innerHTML = threeStars;
  } else if (totalClick < 36) {
    const twoStars = `
    <li><i class="fa fa-star"></i></li>
    <li><i class="fa fa-star"></i></li>
    `;
    getStars.innerHTML = twoStars;
  } else {
    const oneStar = `
    <li><i class="fa fa-star"></i></li>
    `;
    getStars.innerHTML = oneStar;
  }
}

// Reset game on button click
function resetGame() {
  document.getElementById('resetgame').onclick = () => {
    window.location.reload(true);
  };
}

/*
 * Create HTML for end of the game pop-up
 * Congratulate player
 * Show number of moves (1 move = 1 guessed pair, or 2 clicks)
 * Show star rating
 * Allow user to replay game (reloads page)
 */
function endGame() {
  // End timer
  clearInterval(currentTime);
  const getEnd = document.getElementById('cont');
  const makeEnd = document.createElement('section');
  makeEnd.className = 'game-over';
  makeEnd.idName = 'end';
  getEnd.appendChild(makeEnd);

  const makeEndInner = `
  <h2>Game Over!</h2>
  <p>Congratulations, you finished the game in <span id="finalmoves"></span> moves!</p>
  <p>Time: <span id="finaltime"></span></p>
  <div id="endscore">
    <span>Score:</span>
    <ul id="endstars">
    </ul>
  </div>
  <button type="button" name="reset-game" id="resetgame">Play Again</button>
  `;

  makeEnd.innerHTML = makeEndInner;
  scoreKeeper();
  resetGame();
}

// Correct cards stay visible
function correct() {
  document.getElementById(`card${storeId[0]}`).classList.add('match');
  document.getElementById(`card${storeId[1]}`).classList.add('match');
  cardContainer[0].classList.remove('notReady');
  pairs += 1;
  if (pairs === 8) {
    endGame();
  }
}

// Incorrect cards reset
function incorrect() {
  document.getElementById(`card${storeId[0]}`).classList.remove('show', 'open', 'incorrect');
  document.getElementById(`card${storeId[1]}`).classList.remove('show', 'open', 'incorrect');
  cardContainer[0].classList.remove('notReady');
}

// Clear results
function clearCards() {
  currentPair = [];
  storeId = [];
  storeFirstClick = [];
  clickNum = 0;
  cardContainer[0].classList.remove('notReady');
}

// Start timer function
function startTimer() {
  ones += 1;
  if (ones < 9) {
    addOnes.innerHTML = `0${ones}`;
  } if (ones > 9) {
    addOnes.innerHTML = ones;
  } if (ones > 99) {
    tens += 1;
    addTens.innerHTML = `0${tens}`;
    ones = 0;
    addOnes.innerHTML = '00';
  } if (tens > 9) {
    addTens.innerHTML = tens;
  } if (tens > 60) {
    minutes += 1;
    addMinutes.innerHTML = `0${minutes}`;
    tens = 0;
    addTens.innerHTML = '00';
    ones = 0;
    addOnes.innerHTML = '00';
  }
}

/*
 * Compares classes of two cards to see if they match
 * If match, add match class and have cards stay flipped
 * If no match, reset array and re-flip card to back
 */
function checkCards() {
  // Cards match
  if (currentPair[0] === currentPair[1]) {
    // Add match class to cards
    setTimeout(() => {
      document.getElementById(`card${storeId[0]}`).classList.add('correct');
      document.getElementById(`card${storeId[1]}`).classList.add('correct');
    }, 500);
    setTimeout(() => {
      correct();
      clearCards();
    }, 1000);
  } else if (currentPair[0] !== currentPair[1]) {
    // Cards don't match. Reset array, flip cards back
    setTimeout(() => {
      document.getElementById(`card${storeId[0]}`).classList.add('incorrect');
      document.getElementById(`card${storeId[1]}`).classList.add('incorrect');
    }, 500);
    setTimeout(() => {
      incorrect();
      clearCards();
    }, 1000);
  }
}

/*
 * Shows contents of card when clicked on
 * Temporarily stores clicked cards in array to find match
 * If two cards match, they stay showing and change color
 * If two cards do not match, they flip back and reset
 */
function flipCards() {
  cardId.map((i) => {
    const clickMe = document.getElementById(`card${i}`);
    clickMe.onclick = (event) => {
      // Start timer on FIRST click (beginning of game)
      if (totalClick === 0) {
        currentTime = setInterval(startTimer, 10);
      }
      // Remove a star after 14 guesses
      if (totalClick > 28) {
        document.getElementById('secondstar').style.display = 'none';
      }
      // Remove a star after 18 guesses
      if (totalClick > 36) {
        document.getElementById('thirdstar').style.display = 'none';
      }

      // Show clicked card and store value
      event.target.classList.toggle('show');
      event.target.classList.toggle('open');
      clickNum += 1;
      totalClick += 1;
      storeId.push(i);
      storeFirstClick.push(event.target);
      currentPair.push(event.target.children[0].className);

      // Show second clicked card; check if it matches first card or not
      if (clickNum === 2 && event.target === storeFirstClick[0]) {
        cardContainer[0].classList.add('notReady');
        clearCards();
      } else if (clickNum === 2) {
        cardContainer[0].classList.add('notReady');
        checkCards();
      }

      // Update number of moves with each guessed pair
      if (totalClick % 2 === 0) {
        document.getElementById('moves').innerHTML = (totalClick / 2).toString();
      }
    };
    return i;
  });
}

// Load all functions
window.onload = () => {
  shuffle(array);
  dealCards();
  flipCards();
};
