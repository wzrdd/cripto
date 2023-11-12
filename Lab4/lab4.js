// ==UserScript==
// @name         Lab4 - Cripto
// @description  Find secret msg on https://cripto.tiiny.site/
// @version      0.1
// @match        https://cripto.tiiny.site/
// @icon         http://www.tampermonkey.net/favicon.ico
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// ==/UserScript==

(function() {
    // Step 1: Find key
    let key = document.querySelector('p').textContent.match(/[A-Z]/g).join("")
    console.log("La llave es: ", key)

    // Step 2: Find qty of msg.
    let msgs = document.querySelectorAll('div')
    console.log("Los mensajes cifrados son: ", msgs.length)

    // Step 3: Decrypt msgs
    // Parse plaintext key to base64
    let keyBase64 = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(key))
    let parsedKey = CryptoJS.enc.Base64.parse(keyBase64)

    let plainTextDecryptedMsgs = []
    msgs.forEach(msg => {
        let bytesDecryptedMsg = CryptoJS.TripleDES.decrypt(msg.id, parsedKey, {mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7})
        let plainTextDecryptedMsg = CryptoJS.enc.Utf8.stringify(bytesDecryptedMsg)
        plainTextDecryptedMsgs.push(plainTextDecryptedMsg)
        console.log(msg.id, plainTextDecryptedMsg)
    })

    // Step 4: pwned.
    plainTextDecryptedMsgs.forEach(plainTextMsg => {
        let p = document.querySelector("p");
        p.innerHTML += '<br>' + plainTextMsg;
    })
})();
