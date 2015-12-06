$(function(){
    $('#world-map').vectorMap({
                                map: 'world_mill',
                                backgroundColor: "#222",
                                selectedRegions: country_code,
                                regionStyle: {
                                                initial: {
                                                    "fill": '#888'
                                                },
                                                hover: {
                                                    "fill": '#EEE'
                                                },
                                                selected: {
                                                    'fill': '#ffee58'
                                                },
                                            }
                            });
});
