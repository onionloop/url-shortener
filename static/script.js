async function sendURL(){

    const url = document.getElementById("url_input").value;
    
    if (!url){
        document.getElementById("error").innerHTML="Please enter a URL";
        return;
    }

    
try{
    const response = await fetch('/shorten',{
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({url: url})
});

    const result = await response.json();

    const shortURL = document.getElementById("short_link");
    const fullURL = window.location.origin + "/" + result.short_url;
    const displayURL = `tinylink.io/${result.short_url}`;
     
    shortURL.href = fullURL;
    shortURL.textContent= displayURL;
    document.getElementById("url_result").style.display = "block";
    copyButton.disabled = false;
    

    document.getElementById("error").innerHTML = "";
    
}
    catch(error){
        document.getElementById("error").innerHTML = "Something went wrong..."
    }

    
}

const inputField = document.getElementById("url_input");
const copyButton = document.getElementById("copy_button");
const textToCopy = document.getElementById("short_link");
copyButton.disabled = true;


document.getElementById("url_input").addEventListener("keydown", function(e){
    if(e.key == "Enter"){
    

    sendURL();
    inputField.value = '';
    inputField.focus();
    e.preventDefault();
    
}});

document.getElementById("button_clicked").addEventListener("click", function(e){

    sendURL();
    inputField.value = '';
    inputField.focus();
    e.preventDefault();
});



copyButton.addEventListener("click", async() =>{
    const text = textToCopy.href;

    try{
        await navigator.clipboard.writeText(text);

        copyButton.textContent = "Copied!";
    

    setTimeout(() => {
        copyButton.textContent = "Copy"}, 2000)

    } catch (err) {
        console.error('Failed to copy text: ', err);
        alert('Failed to copy text: ' + err); 
    }

});
