const categories = document.querySelectorAll('.seriesView .displayName');
const levels = document.querySelectorAll('.seriesView .iconHolder .index');

categories.forEach((categoryElement) => {
  const categoryName = categoryElement.textContent.trim();
  const levelElements = categoryElement.nextElementSibling.querySelectorAll('.index');

  levelElements.forEach((levelElement) => {
    const levelNumber = levelElement.querySelector('.indexNum').textContent;
    console.log(`| ${categoryName} | ${levelNumber} |`);
  });
});