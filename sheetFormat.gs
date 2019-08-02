function change2Workshops() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getActiveSheet();
  
  var work = sheet.getRange(5, 20);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor(work.getFontColor()); 
  cell.setBackground(work.getBackground()); 
  cell.setFontStyle(work.getFontStyle());

}

function change2Speakers() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getActiveSheet();
  
  var speak = sheet.getRange(6, 20);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor(speak.getFontColor()); 
  cell.setBackground(speak.getBackground()); 
  cell.setFontStyle(speak.getFontStyle());
  
}

function change2Going() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getActiveSheet();
  
  var Personal = sheet.getRange(10, 32);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor(Personal.getFontColor()); 
  cell.setBackground("#b7e1cd");   
}

function change2Low() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getSheetByName("Results");
  
  var Personal = sheet.getRange(11, 32);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setBackground("#a4c2f4");   
}
function change2four() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getSheetByName("Results");
  
  var Personal = sheet.getRange(12, 32);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor("#434343"); 
  cell.setBackground("#f4cccc");   
}

function change2three() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getSheetByName("Results");
  
  var Personal = sheet.getRange(13, 32);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor("#434343"); 
  cell.setBackground("#fce5cd"); 
  
}

function change2two() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getSheetByName("Results");
  
  var Personal = sheet.getRange(14, 32);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor("#434343"); 
  cell.setBackground("#d9d9d9"); 
  
}

function change2Personal() {
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getActiveSheet();
  
  var Personal = sheet.getRange(3, 20);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor(Personal.getFontColor()); 
  cell.setBackground(Personal.getBackground()); 
  cell.setFontStyle(Personal.getFontStyle());
  
}

function change2Conflict(){
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getActiveSheet();
  
  var Conflict = sheet.getRange(40, 14);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor(Conflict.getFontColor()); 
  cell.setBackground(Conflict.getBackground()); 
  cell.setFontStyle(Conflict.getFontStyle());
}

function change2Chosen(){
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getActiveSheet();
  
  var Chosen = sheet.getRange(40, 15);
  
  var cell = sheet.getActiveRange(); 
  
  cell.setFontColor(Chosen.getFontColor()); 
  cell.setBackground(Chosen.getBackground()); 
  cell.setFontStyle(Chosen.getFontStyle());
}

function notesAndFormat(){
  
  showNotes();
  quoteFormat();
  
}

function showNotes(){
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getActiveSheet();
  
  var list = sheet.getRange(1, 24); 
    
  for (var i = 1; i <= 32; i++){
    
    var cell = sheet.getRange(i, 24);
    var values = cell.getValues();

    
    if (values.toString() == "AI"){
      cell.setNote("Friday: 10:00 - 18:30, Saturday: 10:00 - 18:30, Sunday: 10:00 - 14:00");
    }
  }
  
}


// broken could fix with: https://stackoverflow.com/questions/14991030/get-value-in-one-column-in-spreadsheet-using-google-apps-script
//function emailList(){
//  var app = SpreadsheetApp;
//  var Results = app.getActiveSpreadsheet().getSheetByName("Results");
//  
//  var cell = Results.getRange(2, 31);
//  
//  var Responses = app.getActiveSpreadsheet().getSheetByName("Form Responses");
//  var emails = Responses.getColumnGroup(2, 44);
//  
//    cell.setNote(emails);
//
//}


function quoteFormat(){
  var app = SpreadsheetApp;
  var sheet = app.getActiveSpreadsheet().getActiveSheet();
  sheet.getRange(3, 2, 31, 18).setHorizontalAlignment("left");
  
  for(var row = 3; row <= 38; row++){
    for(var col = 2; col <= 18; col++){
      
      var cell = sheet.getRange(row, col);
      var values = cell.getValues();
      var up = sheet.getRange(row - 1, col); 
      
      if(cell.getValue() == '"'){
        cell.setFontColor(up.getFontColor());
        sheet.getRange(row, col).setHorizontalAlignment("center"); 
      }
      
      if(cell.getValue() == '^---- OR'){
        cell.setHorizontalAlignment("right");
//        cell.setFontColor("#b45f06");           // satisfied automatically with cond. format. when "----" appear anywhere in range
      }
      
      
//      if(cell.getFontColor() == "#b45f06"){
//        cell.setHorizontalAlignment("right");
//      }
      
//      else if(values.indexOf('OR')){
//        sheet.getRange(row, col).setHorizontalAlignment(cell.getHorizontalAlignment());
//      }
    }
  }
  
}
  



