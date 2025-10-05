// ===============================
// Photoshop JSX: Run Encrypted File
// ===============================

// Prompt user to select a binary-encoded file
var binFile = File.openDialog("Select Binary Encoded JSX File", "*.bin");
if (binFile == null) {
    alert("No file selected!");
} else {
    binFile.open("r");
    var binaryContent = binFile.read();
    binFile.close();

    // Function to decode binary string to text
    function decodeFromBinary(binaryText) {
        try {
            var binaryValues = binaryText.split(" ");
            var asciiChars = [];
            for (var i = 0; i < binaryValues.length; i++) {
                asciiChars.push(String.fromCharCode(parseInt(binaryValues[i], 2)));
            }
            return asciiChars.join("");
        } catch (e) {
            return null;
        }
    }

    var decodedJSX = decodeFromBinary(binaryContent);

    if (decodedJSX == null) {
        alert("Failed to decode the file. Invalid binary format.");
    } else {
        try {
            // Evaluate the decoded JSX code
            eval(decodedJSX);
        } catch (e) {
            alert("Error running the decoded JSX: " + e.message);
        }
    }
}
