const base = {
    get() {
        return {
            url : "http://localhost:8080/djangovcsvj/",
            name: "djangovcsvj",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "网络求职招聘系统"
        } 
    }
}
export default base
