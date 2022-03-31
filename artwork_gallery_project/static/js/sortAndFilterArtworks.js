const updateURLPath = () => {
  const selectElement = document.getElementById("filter");
  const sortElement = document.querySelector("#sort");
  let url = new URLSearchParams(window.location.search);
  watchEventSort(url, sortElement);
  watchEventCategory(url, selectElement);
};

const watchEventSort = (url, sortElement) => {
  return sortElement.addEventListener("click", (event) => {
    updateSortParam(url);
  });
};

const watchEventCategory = (url, selectElement) => {
  return selectElement.addEventListener("change", (event) => {
    updateCategoryParam(url, event);
  });
};

const updateSortParam = (url) => {
  query_sort = url.get("sort");
  url.set("sort", updateSortValue(query_sort));
  window.location.href = `?${url.toString()}`;
};

// TODO : fix if isnan remove category
const updateCategoryParam = (url, event) => {
  if (isNaN(parseInt(event.target.value))) {
    url.delete("category");
  } else {
    url.set("category", parseInt(event.target.value));
  }

  window.location.href = `?${url.toString()}`;
};

let updateSortValue = (sort_value) => {
  return sort_value == "ASC" || undefined ? "DESC" : "ASC";
};

updateURLPath();
