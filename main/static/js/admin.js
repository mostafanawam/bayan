

function toggleContent(element) {
    const shortContent = element.previousElementSibling.previousElementSibling;
    const moreContent = element.previousElementSibling;
    if (moreContent.style.display === "none") {
        moreContent.style.display = "inline";
        shortContent.style.display = "none";
        element.innerText = "Read less";
    } else {
        moreContent.style.display = "none";
        shortContent.style.display = "inline";
        element.innerText = "Read more";
    }
}


