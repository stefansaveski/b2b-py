
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

async function submitCode() {
  var currentPageName = window.location.pathname.replace(/\/$/, '').split('/').pop();
  const code = document.getElementById('code').value;
  var jsonData = {
      "cpp_code": code.replace(/\n/g, "\n"),
      "zadaca": currentPageName
  };
  console.log(jsonData)
  try {
      const response = await fetch('/process_code', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ jsonData }),
      });

      const data = await response.json()
      console.log(data)
      return data;
     // document.getElementById('result').innerText = 'Result: ${data.result}';
  } catch (error) {
      console.error('Error:', error);
  }
}

async function displayDataInTable() {
  var location = document.getElementById("results");

  location.innerHTML = '<div class="loader"></div>';
  jsonData = await submitCode();
  try {
    var table = document.createElement("table");
    table.style.borderCollapse = "collapse"; 
    location.innerHTML = "";
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
      var row = table.insertRow();
      var resultCell = row.insertCell();
      resultCell.style.padding = "12px";
      resultCell.colSpan = 3; 
      resultCell.style.border = "1px solid black"; 
      resultCell.style.color = "red";
      resultCell.style.fontWeight = "800";
      resultCell.appendChild(document.createTextNode("Didn't pass all tests."));
    }
    location.appendChild(table);
  } catch (error) {
    console.error("Error in displayDataInTable:", error);
  }
}
