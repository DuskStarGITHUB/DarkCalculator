function copyToClipboard() {
    var emailAddress = "contactspeencer@gmail.com";
    var dummyInput = document.createElement("input");
    dummyInput.setAttribute("value", emailAddress);
    document.body.appendChild(dummyInput);
    dummyInput.select();
    document.execCommand("copy");
    document.body.removeChild(dummyInput);

    alert("Dirección de correo copiada al portapapeles: " + emailAddress);
}