function onBuild (doneCB) {
    return (err, stats) => {
        if (err) {
            console.log('Error', err);
            process.exit();
            return;
        } else {
            stats.stats.forEach((stat) => {
                Object.keys(stat.compilation.assets).forEach((key) => {
                    console.log('Webpack output:', key);
                });
            });
            if (doneCB) {
                doneCB();
            }
        }
    }
}