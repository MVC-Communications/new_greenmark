window.jsPDF = window.jspdf.jsPDF;

var doc = new jsPDF();
	
// Source HTMLElement or a string containing HTML.
var elementHTML = document.querySelector("#contnet");

doc.html(elementHTML, {
    callback: function(doc) {
        // Save the PDF
        doc.save('sample-document.pdf');
    },
    x: 15,
    y: 15,
    width: 170, //target width in the PDF document
    windowWidth: 650 //window width in CSS pixels
});

var doc = new jsPDF({
    orientation: 'landscape'
});

doc.text(20, 20, 'Hello world!');
doc.text(20, 30, 'This is client-side Javascript to generate a PDF.');

// Add new page
doc.addPage();
doc.text(20, 20, 'Visit CodexWorld.com');
