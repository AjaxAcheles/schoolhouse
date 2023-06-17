//pyscript.runtime.globals.get('<varname>') this gets the value of 'varname' in the python file when called.

function print(statement) {
    var output = document.createElement("p");
    $(output).text(statement);
    document.getElementById("output").appendChild(output);
    return output;
}

async function input(prompt) {
    var isEnterPressed = false; 

    function addRepl() {
        var inputElement = document.createElement("input");
        $(inputElement).attr("type", type);
        document.getElementById("output").appendChild(inputElement);
        return inputElement;
    }

    print(prompt);
    var inputElemnt = addRepl("text");

    function waitingEnterPressed() {
        return new Promise((resolve) => {
          document.addEventListener('keydown', onKeyHandler);

          function onKeyHandler(e) {
            if (e.keyCode === 13) {
              document.removeEventListener('keydown', onKeyHandler);
              resolve();
            }
          }

        });
      }

    await waitingEnterPressed();
    
    var userInput = $(inputElemnt).text();
    return userInput;
}

