//BELOTINDOS, JOHN RAFAEL P. 
//SECTION G-1L
//This code is the circuitry of belotindos_ex9.html

//FETCHER - This part of the code fetches necessary datas in the html file
const bedroom = document.getElementById("bedroom");
const bedsize = document.getElementsByName("bedsize");
const childroom = document.getElementById("child");
const cabinet = document.getElementsByName("cabinets");
const tables = document.getElementsByName("tables");
const decors = document.getElementsByName("decor");
const roomsize = document.getElementById("roomsize");
const roomtype = document.getElementsByName("roomtype")
const stop = document.getElementById("calculate")
const pickup = document.getElementById("pickup")
const delivery = document.getElementsByName("deliver");
const deliver = document.getElementById("delivery")

//DISABLER - This function disables certain bed sizes depending on the room type. It also disables the delivery informations if it is not selected.
function thisable(){
    if (bedroom.checked){
    for (var i=0; i<bedsize.length; i++){
        bedsize[i].disabled = false;
                                        }
                        }
    else{
        for (var i=0; i<bedsize.length; i++){
        bedsize[i].disabled = true;
                                            }
        }
 
    if (deliver.checked){
        for (var i=0; i<delivery.length;i++){
            delivery[i].disabled=false
                                            }
                         }
    else{
        for (var i=0; i<delivery.length;i++){
            delivery[i].disabled=true
                                            }
        }
                    }

function thisableforchild(){ //I seperated this function because it blends with the bedroom in thisable().
       if (childroom.checked){
        bedsize[0].disabled=false
        bedsize[1].disabled=false
        bedsize[2].disabled=true
        bedsize[3].disabled=true
       }
                               
}
//LISTENERS FOR THISABLE()
document.getElementById("bedroom").addEventListener("change",thisable) //https://www.w3schools.com/js/js_htmldom_eventlistener.asp - This code listens to changes in the html and executes a function.
document.getElementById("living").addEventListener("change",thisable)
document.getElementById("office").addEventListener("change",thisable)
document.getElementById("child").addEventListener("change",thisableforchild) //different function to work properly on every scenario.
document.getElementById("delivery").addEventListener("change",thisable)
document.getElementById("pickup").addEventListener("change",thisable)
thisable()

//DATES
const input_date = document.getElementById("deliverydate")
const error_date = document.getElementById("pastdate")
function sureness(){ //This function checks the input date and time to make sure it is valid.
if (pickup.checked){stop.disabled=false}
else if (deliver.checked){datevalidator()}}
function datevalidator(){
    let current_date= new Date()
    let delivery_date = new Date(input_date.value)
    if (delivery_date<current_date){
        error_date.textContent = "Provide a future date."
        stop.disabled=true //This disables the submit button until the user inputs a valid date and time
                                      }
    else {
        error_date.textContent = ""
        stop.disabled=false
         }
    timevalidator()
                        }

let time = document.getElementById("deliverytime")
const badtime = document.getElementById("satamangpanahon")//This is an id for a <p> in html
function timevalidator(){
    updatedtime = time.value
    if (updatedtime < "09:00" || updatedtime > "18:00"){
        badtime.textContent = "Select a time between 9AM and 6PM."
        stop.disabled=true

                                                        }
    else{
        badtime.textContent = ""
        stop.disabled=false
        }
                        }
    
//EVENT LISTENER FOR DELIVERIES
document.getElementById("deliverydate").addEventListener("change", sureness)
document.getElementById("deliverytime").addEventListener("change", sureness)
pickup.addEventListener("change",sureness)

//THE CONTAINER - This contains the values of the selected inputs.
let bedsizevalue = 0
let cabinetvalue = 0
let tablevalue=0
let decorvalue=0
let roomsizevalue = 0
let room_setup = 0
let deliverycost = 0 
let textroomtype = ""
let textbedsize = ""
let textcabinet =""
let texttables = []
let textdecor = []
let textroomsize = ""
let textroomsizer = "" 
//THE RESSETER - This resets the container on every submit, so that values doesnt stack.
function resetter(){
bedsizevalue = 0
cabinetvalue = 0
tablevalue=0
decorvalue=0
deliverycost=0
textroomtype = ""
textbedsize = ""
textcabinet =""
texttables =[]
textdecor = []
textroomsize = ""
getvalues()
}
//THE VALUE GETTER - This identifies the inputs that the users checked and changes the values in the container/
function getvalues(){
if (bedroom.checked||childroom.checked){
for (var i=0; i<bedsize.length; i++){
    if (bedsize[i].checked){
        bedsizevalue = parseInt(bedsize[i].value)
                           }
                             }
                            }
else{bedsizevalue=0}
//CABINETS                           
for (var i=0; i<cabinet.length; i++){
    if (cabinet[i].checked){
        cabinetvalue = parseInt(cabinet[i].value)
                    }
                }
            
//TABLES
for (var i=0; i<tables.length; i++){
    if (tables[i].checked){
        tablevalue += parseInt(tables[i].value)
                    }
                }
            
//DECORATIONS
for (var i=0; i<decors.length; i++){
    if (decors[i].checked){
        decorvalue += parseInt(decors[i].value)
                    }
                }
roomsizevalue = parseFloat(roomsize.value)
if (deliver.checked){
    deliverycost = 1000
}
discount()
            }
            
// DISCOUNTER - This discounts the tables based on the amount of tables selected. I based it on price since maximum possible values of different amount of tables (like 2 tables can have a max possible value of 10500) doesnt overlap.
function discount(){
    if(tablevalue==28500){tablevalue = tablevalue*0.75}
    else if(tablevalue>=18500){tablevalue = tablevalue*0.85}
    else if(tablevalue>=10500){tablevalue = tablevalue*0.9}
        calculate()}

function calculate(){//This is the main formula
room_setup=((bedsizevalue+cabinetvalue+decorvalue+tablevalue)*roomsizevalue)+deliverycost
summary()}

function debug(){
console.log("Bed" + bedsizevalue)
console.log("Cabinet" + cabinetvalue)
console.log("Table" + tablevalue)
console.log("Decor" + decorvalue)
console.log("Room Size"+roomsizevalue)
console.log("Delivery Cost"+deliverycost)
console.log("Total"+room_setup)
console.log(textroomsize) }
//TEXT PLACEHOLDERS

function summary(){
    for (i=0; i<roomtype.length;i++){if(roomtype[i].checked){textroomtype=roomtype[i].labels[0].textContent}} //https://www.reddit.com/r/learnjavascript/comments/t4lnt0/comment/hyza1rv/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    if (bedroom.checked||childroom.checked){for (i=0; i<bedsize.length;i++){if(bedsize[i].checked){textbedsize=bedsize[i].labels[0].textContent}}} else{textbedsize="N/A"}
    for (i=0; i<cabinet.length;i++){if(cabinet[i].checked){textcabinet=cabinet[i].labels[0].textContent}}//This gets the Label Text 
    for (i=0; i<tables.length;i++){if(tables[i].checked){texttables.push(tables[i].labels[0].textContent)}}
    for (i=0; i<decors.length;i++){if(decors[i].checked){textdecor.push(decors[i].labels[0].textContent)}}
    foralertdecor = textdecor.join(" | ") 
    foralerttable = texttables.join(" | ") //https://www.w3schools.com/jsref/jsref_join.asp -  This joins the list in texttables.
    textroomsize = roomsize.options[roomsize.selectedIndex].text //https://stackoverflow.com/questions/14976495/get-selected-option-text-with-javascript - This gets the text in the selected value.
    
    if (deliver.checked){//This is the alert message with delivery
    alert("[Customer Information]"+"\n"+"Name: "+ document.getElementById("name").value+"\n"+
    "Mobile Number: "+document.getElementById("mobilenumber").value+"\n"+
    "Email: "+document.getElementById("email").value+"\n"+'\n'+
    "[ITEA Room Setup Details]"+"\n"+
    "Number of occupants: "+ document.getElementById("occupants").value+'\n'+
    "Room Type: "+textroomtype+'\n'+
    "Bed Size: "+ textbedsize +'\n'+
    "Cabinets: "+ textcabinet + '\n'+
    "Tables: "+ foralerttable +'\n'+'\n'+
    "Decorative Additions: " + foralertdecor + '\n' +
    "Room Size: "+textroomsize+'\n'+'\n'+
    "With delivery adding P1000."+'\n'+
    "Total cost of room setup: P"+room_setup
    )}
    else {alert("[Customer Information]"+"\n"+"Name: "+ document.getElementById("name").value+"\n"+ //This is the alert message without delivery
    "Mobile Number: "+document.getElementById("mobilenumber").value+"\n"+
    "Email: "+document.getElementById("email").value+"\n"+'\n'+
    "[ITEA Room Setup Details]"+"\n"+
    "Number of occupants: "+ document.getElementById("occupants").value+'\n'+
    "Room Type: "+textroomtype+'\n'+
    "Bed Size: "+ textbedsize +'\n'+
    "Cabinets: "+ textcabinet + '\n'+
    "Tables: "+ foralerttable +'\n'+'\n'+
    "Decorative Additions: " + foralertdecor + '\n' +
    "Room Size: "+textroomsize+'\n'+'\n'+
    "Total cost of room setup: P"+room_setup
    )}
    debug()
}

const antireset = document.getElementById('form');
antireset.addEventListener('submit', function(event) {event.preventDefault();resetter()})

