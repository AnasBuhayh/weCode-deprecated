const Posts = {
    data() {
        return {
            posts: [],
            currentPage: 1,
            hasNext: true

        }
    },
    delimiters: ['[[', ']]'],
    mounted() {
        this.getPosts()

        window.onscroll = () => {
            let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight

            if (bottomOfWindow && this.hasNext) {
                this.currentPage += 1
                this.getPosts()
            }
        }
    },
    methods: {
        getPosts() {
            console.log('Get Posts')

            fetch(`/get_posts/?page=${this.currentPage}`)
                .then(response => {
                    return response.json()
                })
                .then(data => {

                    this.hasNext = false

                    if(data.next) {
                        this.hasNext = true
                    }

                    for (let i = 0; i < data.results.length; i++) {
                        this.posts.push(data.results[i])
                    }
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
Vue.createApp(Posts).mount('#posts')