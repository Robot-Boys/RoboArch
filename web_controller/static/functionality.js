function changePose (pose) {
    console.log("a js pose:", pose);
    axios.put('/pose/' + pose)
        .then(function (succes) {
            console.log("pose puted");
        }
    ).catch(function (error) {
        console.log('put failed', error);
    });
}