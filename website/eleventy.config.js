module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy("src/scripts");
    eleventyConfig.addPassthroughCopy("src/styles");
    eleventyConfig.addPassthroughCopy("src/assets");
    eleventyConfig.addPassthroughCopy({"node_modules/@picocss/pico/css/pico.jade.min.css" : "styles/pico.jade.min.css"});

    return {
        dir: {
          input: 'src',
          layouts: '_includes'
        }
      };
};