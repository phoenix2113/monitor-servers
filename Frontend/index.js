const serverName = document.getElementById("serverName")
const urlS = document.getElementById("urlS")
const freq = document.getElementById("freq")
const server1 = document.getElementById("server1")
const serverTag = document.getElementById("serverTag")
const allValuesArr = []

function downloadCSV(csv, filename) {  
    let csvFile;  
    let downloadLink;  
    //define the file type to text/csv  
    csvFile = new Blob([csv], {type: 'text/csv'});  
    downloadLink = document.createElement("a");  
    downloadLink.download = filename;  
    downloadLink.href = window.URL.createObjectURL(csvFile);  
    downloadLink.style.display = "none";  
  
    document.body.appendChild(downloadLink);  
    downloadLink.click();  
}  
  
//user-defined function to export the data to CSV file format  
function exportTableToCSV(filename,csvFields) {  
   //declare a JavaScript variable of array type  
  const csv = []  
  csv.push(csvFields.join(","));  
   //call the function to download the CSV file  
   downloadCSV(csv.join("\n"), filename);  
}  

function submitForm(e){
    e.preventDefault()
    const {serverName, urlS, freq, server1, serverTag} = e.target.elements
    exportTableToCSV('table1.csv',[allValuesArr])
    exportTableToCSV('table2.csv',[server1,serverTag])
}

const saveValue = () => {
    const serverName = document.getElementById("serverName").value
    const urlS = document.getElementById("urlS").value
    const freq = document.getElementById("freq").value
    const server1 = document.getElementById("server1").value
    const serverTag = document.getElementById("serverTag").value
    allValuesArr.push({serverName,urlS, freq, server1, serverTag})
}