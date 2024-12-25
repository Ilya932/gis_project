
function scrollToBlock(blockId) {
  const element = document.getElementById(blockId);

  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
    history.pushState(null, '', window.location.pathname);
  }
}