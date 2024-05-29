
function get_AspectRatio(img) {
    return img.height / img.width;
}

function convert_HtmlImageElement_to_ImageDate(oimg) {
    var img=new Image();
    img.src=oimg.src;
    img.crossOrigin = "anonymous";
    var canvas = document.createElement('canvas');
    canvas.width = img.width;
    canvas.height = img.height;
    var ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);
    var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    return imageData;
}

function get_InfoDensity(img) {
    imageData = convert_HtmlImageElement_to_ImageDate(img);

    return 0;

    const grayValues = new Array(256).fill(0);
    const totalPixels = imageData.width * imageData.height;

    for (let i = 0; i < totalPixels; i++) {
        const grayValue = Math.floor(
            (imageData.data[i * 4] + imageData.data[i * 4 + 1] + imageData.data[i * 4 + 2]) / 3
        );
        grayValues[grayValue]++;
    }

    const probabilities = grayValues.map((value) => value / totalPixels);
    const informationContent = probabilities.map((probability) => -probability * Math.log2(probability));
    const entropy = informationContent.reduce((sum, value) => sum + value, 0);

    return entropy;
}



var images = document.getElementsByTagName("img");
console.log(images);
for (var i = 0; i < images.length; i++) {
    img = images[i];

    ar = get_AspectRatio(img);
    ind = get_InfoDensity(img);

    console.log("高宽比: ", ar, " 信息密度: ", ind);
}

