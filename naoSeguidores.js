(function(console){
    console.save = function(data, filename){
        if(!data) {
            console.error('Console.save: No data')
            return;
        }
        if(!filename) filename = 'naoSeguidores.json'
        if(typeof data === "object"){
            data = JSON.stringify(data, undefined, 4)
        }
        var blob = new Blob([data], {type: 'text/json'}),
            e    = document.createEvent('MouseEvents'),
            a    = document.createElement('a')
        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
        e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        a.dispatchEvent(e)
     }
})(console)

function naoSeguidores() {
    var total = document.querySelector("body > div.modal > div > div > div > div.result").childElementCount;
    console.log(total);

    arr = [];

    for (var i = 0; i < total; i++) {
        href = document.querySelector("body > div.modal > div > div > div > div.result").children[i].children[0].getAttribute('href');
        arr.push(href)
    }
    console.save(arr);
}

naoSeguidores()