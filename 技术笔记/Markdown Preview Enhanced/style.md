<style>
img{
    width: 60%;
    padding-left: 20%;
}
</style>

<script>
var images = document.getElementsByTagName("img");
console.log(images);
for (var i = 0; i < images.length; i++) {
    if (img.width / img.height > 1) {
    img = images[i];
    img.style.width='30px';
    console.log(img.style.width);
    }
}
</script>

<script>

var img = new Image();
img.src = 'path/to/image.png';
img.onload = function() {
  // 图像加载完成后执行的代码
};

var canvas = document.createElement('canvas');
var ctx = canvas.getContext('2d');
ctx.drawImage(img, 0, 0, img.width, img.height);

var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
var pixels = imageData.data;

// 遍历像素数据，统计每个颜色的出现次数，计算颜色直方图。

var colorCounts = {};
var colorHistogram = [];
for (var i = 0; i < pixels.length; i += 4) {
  var r = pixels[i];
  var g = pixels[i + 1];
  var b = pixels[i + 2];
  var a = pixels[i + 3];
  var color = 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')';
  if (colorCounts[color]) {
    colorCounts[color]++;
  } else {
    colorCounts[color] = 1;
  }
}
for (var color in colorCounts) {
  colorHistogram.push({
    color: color,
    count: colorCounts[color]
  });
}

// 计算颜色均值和标准差。

var colorSum = {
  r: 0,
  g: 0,
  b: 0,
  a: 0
};
for (var i = 0; i < pixels.length; i += 4) {
  colorSum.r += pixels[i];
  colorSum.g += pixels[i + 1];
  colorSum.b += pixels[i + 2];
  colorSum.a += pixels[i + 3];
}
var colorMean = {
  r: colorSum.r / (pixels.length / 4),
  g: colorSum.g / (pixels.length / 4),
  b: colorSum.b / (pixels.length / 4),
  a: colorSum.a / (pixels.length / 4)
};
var colorStd = {
  r: 0,
  g: 0,
  b: 0,
  a: 0
};
for (var i = 0; i < pixels.length; i += 4) {
  colorStd.r += Math.pow(pixels[i] - colorMean.r, 2);
  colorStd.g += Math.pow(pixels[i + 1] - colorMean.g, 2);
  colorStd.b += Math.pow(pixels[i + 2] - colorMean.b, 2);
  colorStd.a += Math.pow(pixels[i + 3] - colorMean.a, 2);
}
colorStd.r = Math.sqrt(colorStd.r / (pixels.length / 4));
colorStd.g = Math.sqrt(colorStd.g / (pixels.length / 4));
colorStd.b = Math.sqrt(colorStd.b / (pixels.length / 4));
colorStd.a = Math.sqrt(colorStd.a / (pixels.length / 4));

</script>


计算图片的信息熵可以通过以下步骤实现：

将图片转换为灰度图像。
计算灰度图像中每个像素的灰度值。
计算灰度值的频率。
计算每个灰度值的概率。
计算每个灰度值的信息量。
计算所有灰度值的信息熵。

<script>
function calculateEntropy(imageData) {
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
</script>

