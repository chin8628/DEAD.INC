$(function(){
    $('#world-map').vectorMap({
                                map: 'world_mill',
                                backgroundColor: "#222",
                                regionStyle: {
                                                initial: {
                                                    "fill": 'white'
                                                },
                                                hover: {
                                                    "fill": 'blue',
                                                    "fill-opacity": 0.6,
                                                }
                                                selected: {
                                                    fill: 'yellow'
                                                },
                                            }
                            });
});
