const url = window.location.href

const quizBox = document.getElementById('quiz-box')

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        data.forEach(element => {
            for (const [question, answers] of Object.entries(element)){
                console.log(question)
                console.log(answers)
            }
        });
    },
    error: function (error) {
        console.log(error)
    }
})