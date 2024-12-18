module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy("src/scripts");
    eleventyConfig.addPassthroughCopy("src/styles");
    eleventyConfig.addPassthroughCopy("src/assets");
    eleventyConfig.addPassthroughCopy({"node_modules/@picocss/pico/css/pico.jade.min.css" : "styles/pico.jade.min.css"});

    eleventyConfig.addWatchTarget("!src/assets");

    // Add the folder to BrowserSync's watch list
    eleventyConfig.setBrowserSyncConfig({
      files: ["!src/assets/*/**"], // Watch for changes in the images folder
  });
    return {
        dir: {
          input: 'src',
          layouts: '_includes'
        }
      };
};