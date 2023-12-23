window.onload = loadPage;
async function loadPage(){
  var zadaca = window.location.pathname.replace(/\/$/, '').split('/').pop();
var location = document.getElementById("results");
jsonData = {
  "zadaca": zadaca
}
const response = await fetch('/get_page', {
  method: 'POST',
  headers: {
      'Content-Type': 'application/json',
  },
  body: JSON.stringify({ jsonData }),
});
const data = await response.json()
console.log(data);
if(data.get != "empty"){
  //location.appendChild(data.table);
  document.getElementById('code').value = data.code;

  
  var location = document.getElementById("results");
  jsonData = data.table;
  console.log(jsonData)
  const CE = jsonData.CompilationError;
    try {
      var table = document.createElement("table");
      table.style.borderCollapse = "collapse"; 
      var headerRow = table.insertRow();
      ["Input", "Expected", "Got"].forEach((header) => {
        var th = document.createElement("th");
        th.appendChild(document.createTextNode(header));
        th.style.border = "1px solid black"; 
        th.style.padding = "15px";
        headerRow.appendChild(th);
      });

      let flag = true;
      const keys = Object.keys(jsonData.input);
      const halfLength = Math.ceil(keys.length / 2);
      for (let i = 0; i < halfLength; i++) {
        const key = keys[i];
        var row = table.insertRow();
        row.style.border = "1px solid black"; 

        var inputCell = row.insertCell();
        inputCell.style.border = "1px solid black"; 
        inputCell.style.padding = "10px";
        var inputText = jsonData.input[key].replace(/\n/g, "<br>");
        inputCell.innerHTML = inputText;

        var expectedCell = row.insertCell();
        expectedCell.style.border = "1px solid black";
        expectedCell.style.padding = "10px";
        var expectedText = jsonData.expected[key].replace(/\n/g, "<br>");
        expectedCell.innerHTML = expectedText;

        var gotCell = row.insertCell();
        gotCell.style.border = "1px solid black"; 
        gotCell.style.padding = "10px";
        var gotText = jsonData.got[key].replace(/\n/g, "<br>");
        gotCell.innerHTML = gotText;

        if (jsonData.is_same[key] === "true") {
          row.style.backgroundColor = "lightgreen";
        } else {
          row.style.backgroundColor = "#FFCCCB";
          flag = false;
        }
      }
      if (jsonData.correct == "10") {
        var row = table.insertRow();
        var resultCell = row.insertCell();
        resultCell.style.padding = "12px";
        resultCell.colSpan = 3;
        resultCell.style.border = "1px solid black"; 
        resultCell.style.color = "green";
        resultCell.style.fontWeight = "800";
        resultCell.appendChild(document.createTextNode("Passed all tests!"));
      } else {
        //button.disabled = false;
        var row = table.insertRow();
        var resultCell = row.insertCell();
        resultCell.style.padding = "12px";
        resultCell.colSpan = 3; 
        resultCell.style.border = "1px solid black"; 
        resultCell.style.color = "red";
        resultCell.style.fontWeight = "800";
        resultCell.appendChild(document.createTextNode("Didn't pass all tests"));
      }
      location.appendChild(table);
    } catch (error) {
      console.error("Error in displayDataInTable:", error);
    }


}
}


async function saveInfo(){
  try {
      var firstName = document.getElementById("firstName").value; 
      var lastName = document.getElementById("lastName").value; 
      var index = document.getElementById("indexNumber").value; 
      var jsonData = {
        "index": index,
        "name": firstName + " " + lastName,
      }
      const response = await fetch('/login', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ jsonData }),
      });
  } catch (error) {
      console.error('Error:', error);
  }
}

function checkfields(){
  var firstName = document.getElementById("firstName").value; 
  var lastName = document.getElementById("lastName").value; 
  var index = document.getElementById("indexNumber").value;
  if(firstName == "" || lastName == "" || index == ""){
      alert("Fill all the fields!");
  }
  else{
      location.href = `${window.location.protocol}//${window.location.host}/zadaca1`; 
      saveInfo();
  } 
}

async function submitCode() {
  var currentPageName = window.location.pathname.replace(/\/$/, '').split('/').pop();
  const code = document.getElementById('code').value;
  var jsonData = {
      "cpp_code": code.replace(/\n/g, "\n"),
      "zadaca": currentPageName
  }
  try {
      const response = await fetch('/process_code', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ jsonData }),
      });

      const data = await response.json()
      return data;
     // document.getElementById('result').innerText = 'Result: ${data.result}';
  } catch (error) {
      console.error('Error:', error);
  }
}

async function displayDataInTable(buttonId) {
  var savetable;
  var savecode;
  var location = document.getElementById("results");
  location.innerHTML = '<div class="loader"></div>';
  const button = document.getElementById(buttonId);
  button.disabled = true;
  jsonData = await submitCode();
  const CE = jsonData.CompilationError;
    try {
      var table = document.createElement("table");
      table.style.borderCollapse = "collapse"; 
      location.innerHTML = "";
      if(CE == 'Compilation Error'){
        button.disabled = false;
        location.innerHTML = '<div class="h4" style="color: #780116">Compilation Error</div>';
        return;
      }
      else if(CE == 'Time Limit Exceeded'){
        button.disabled = false;
        location.innerHTML = '<div class="h4" style="color: #780116">Time Limit Exceeded</div>';
        return;
      }
      else if(CE == 'Server error try again'){
        button.disabled = false;
        location.innerHTML = '<div class="h4" style="color: #780116">Server error reload page and try again</div>';
        return;
      }
      var headerRow = table.insertRow();
      ["Input", "Expected", "Got"].forEach((header) => {
        var th = document.createElement("th");
        th.appendChild(document.createTextNode(header));
        th.style.border = "1px solid black"; 
        th.style.padding = "15px";
        headerRow.appendChild(th);
      });

      let flag = true;
      const keys = Object.keys(jsonData.input);
      const halfLength = Math.ceil(keys.length /2);
      for (let i = 0; i < halfLength; i++) {
        const key = keys[i];
        var row = table.insertRow();
        row.style.border = "1px solid black"; 

        var inputCell = row.insertCell();
        inputCell.style.border = "1px solid black"; 
        inputCell.style.padding = "10px";
        var inputText = jsonData.input[key].replace(/\n/g, "<br>");
        inputCell.innerHTML = inputText;

        var expectedCell = row.insertCell();
        expectedCell.style.border = "1px solid black";
        expectedCell.style.padding = "10px";
        var expectedText = jsonData.expected[key].replace(/\n/g, "<br>");
        expectedCell.innerHTML = expectedText;

        var gotCell = row.insertCell();
        gotCell.style.border = "1px solid black"; 
        gotCell.style.padding = "10px";
        var gotText = jsonData.got[key].replace(/\n/g, "<br>");
        gotCell.innerHTML = gotText;

        if (jsonData.is_same[key] === "true") {
          row.style.backgroundColor = "lightgreen";
        } else {
          row.style.backgroundColor = "#FFCCCB";
          flag = false;
        }
      }
      if (jsonData.correct == "10") {
        var row = table.insertRow();
        var resultCell = row.insertCell();
        resultCell.style.padding = "12px";
        resultCell.colSpan = 3;
        resultCell.style.border = "1px solid black"; 
        resultCell.style.color = "green";
        resultCell.style.fontWeight = "800";
        resultCell.appendChild(document.createTextNode("Passed all tests!"));
      } else {
        button.disabled = false;
        var row = table.insertRow();
        var resultCell = row.insertCell();
        resultCell.style.padding = "12px";
        resultCell.colSpan = 3; 
        resultCell.style.border = "1px solid black"; 
        resultCell.style.color = "red";
        resultCell.style.fontWeight = "800";
        resultCell.appendChild(document.createTextNode("Didn't pass all tests"));
      }
      savetable = table;
      savecode = document.getElementById('code').value;
      //console.log(savetable, savecode);
      savePage(jsonData, savecode);
      location.appendChild(table);
    } catch (error) {
      console.error("Error in displayDataInTable:", error);
    }
}

async function savePage(jsonData, code){
  var zadaca = window.location.pathname.replace(/\/$/, '').split('/').pop();
  jsonData = {
    "table": jsonData,
    "cpp_code": code,
    "zadaca": zadaca
  }
  console.log(jsonData);
  const response = await fetch('/save_page', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ jsonData }),
  });
}