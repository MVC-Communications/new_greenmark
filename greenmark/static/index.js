
// 1. allocate the id of the dowload button to a const
// 2. allocate the id of the div you want to dowload to a const

window.onload = function () {
    document.getElementById("download").addEventListener("click", () => {
        const fileToBeDowloaded = this.document.getElementById("fileToBeDowloaded");
        // console.log(fileToBeDowloaded);
        // console.log(window);

        //hence set the options you preffer such as filename and others
        var opt = {
            // margin: 1,
            filename: 'iso_document.pdf'/*file name*/,
            image: { type: 'jpeg', quality: 0.98 },
            html2canvas: { scale: 2 },
            jsPDF: { unit: 'in', format: 'A4', orientation: 'portrait' }
        };

        //hence execute this function to dowload the file
        html2pdf().from(fileToBeDowloaded /* gotten div*/).set(opt).save();
    })
}