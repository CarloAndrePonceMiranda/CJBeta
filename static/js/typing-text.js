console.log("ejecutando typing-text");
// get the element
var text = document.querySelector('.typing-text');

// make a words array
var words = [
    "<?php \n  echo 'Bienvenido a T.E.D.';\n  echo 'La victoria favorece\n   a los que se preparan';\n?>",
    "class HolaTED{\n  public static void main(String args[]){\n   System.out.println(\"Bienvenido a T.E.D.\");\n  }\n}",
    "#Hola T.E.D. en Python\nprint \"Bienvenido a T.E.D.\"",
    "<script type=\"text/javascript\">\n  document.write('Bienvenido a T.E.D.');\n<script>",
    "#Hola T.E.D. en Ruby\nputs\"Bienvenido a T.E.D.\"",
    "Hola T.E.D. en SQL\nSELECT 'Bienvenido a T.E.D.';"
];

// start typing effect
setTyper(text, words);

function setTyper(element, words) {

    var LETTER_TYPE_DELAY = 75;
    var WORD_STAY_DELAY = 2000;

    var DIRECTION_FORWARDS = 0;
    var DIRECTION_BACKWARDS = 1;

    var direction = DIRECTION_FORWARDS;
    var wordIndex = 0;
    var letterIndex = 0;

    var wordTypeInterval;

    startTyping();

    function startTyping() {
        wordTypeInterval = setInterval(typeLetter, LETTER_TYPE_DELAY);
    }

    function typeLetter() {
        var word = words[wordIndex];

        if (direction == DIRECTION_FORWARDS) {
            letterIndex++;

            if (letterIndex == word.length) {
                direction = DIRECTION_BACKWARDS;
                clearInterval(wordTypeInterval);
                setTimeout(startTyping, WORD_STAY_DELAY);
            }

        } else if (direction == DIRECTION_BACKWARDS) {
            letterIndex--;

            if (letterIndex == 0) {
                nextWord();
            }
        }

        var textToType = word.substring(0, letterIndex);

        element.textContent = textToType;
    }

    function nextWord() {

        letterIndex = 0;
        direction = DIRECTION_FORWARDS;
        wordIndex++;

        if (wordIndex == words.length) {
            wordIndex = 0;
        }

    }
}
