document.addEventListener("DOMContentLoaded", function() {
    const nameSearch = document.getElementById("name-search");
    const projects = document.querySelectorAll(".project");
    const tags  = document.querySelectorAll('.tag')
    function filterProject() {
        const nameQuery = nameSearch.value.toLowerCase();

        projects.forEach((project) => {
            const name = project.getAttribute('data-name').toLowerCase();
            const nameMatch = name.includes(nameQuery);

            if (nameMatch) {
                project.style.display = "";
            } else {
                project.style.display = "none";
            }
        });
    }

    tags.forEach((tag) => {
        tag.addEventListener("click", function() {
            const selectedTag = this.getAttribute('data-tag')
            
            projects.forEach((project) => {
                const projectTag = project.getAttribute('data-tags')

                if (projectTag.includes(selectedTag)) {
                    project.style.display = ""
                } else {
                    project.style.display = "none"
                }
            }) 
        })
    })

    

    nameSearch.addEventListener('keyup', filterProject);
});
