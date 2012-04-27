(function( $ ){

    $.fn.mdslide = function(options) {

        var settings = $.extend(options);

        return this.each(function() {
            $.ajax({
                url : settings.src,
                dataType : 'text',
                success : file_loaded
            })
            
            var $container = $(this);
            var md_con = new Showdown.converter();

            function file_loaded(data){
                append($container, data);

                $container.jmpress();
                $container.css("top", "30%");

                $('pre code').each(function(i, e) {hljs.highlightBlock(e, '    ')});
            }

            function find_tag(data, tag){
                var index = -1;
                var tag_list = [];
                while((index = data.indexOf(tag, index+1)) != -1){
                    
                    if(index > 0 && data[index-1] != "\n"){
                        continue;
                    }

                    tag_list.push({t: tag, i: index})
                }
                return tag_list;
            }

            function get_slides(data){
                var tag_list = [];
                
                tag_list = tag_list.concat(find_tag(data, "\{"));
                tag_list = tag_list.concat(find_tag(data, "\}"));
                tag_list = tag_list.concat(find_tag(data, "\""));

                tag_list.sort(function(a, b){
                    return (a.i - b.i);
                });

                var slides = [];
                var slide;
                var parent;
                var inString = false;

                for(var i in tag_list){
                    
                    var tag = tag_list[i].t;
                    var index = tag_list[i].i;
                    
                    if(!inString && tag == "\{"){
                        if(slide){
                            parent = slide;
                        }

                        slide = {};
                        slide.children = []
                        slide.start = index;
                        
                        if(parent){
                            slide.parent = parent;
                        }
                    }

                    if(!inString && tag == "\}"){

                        if(!slide){
                            return;
                        }

                        slide.end = index;

                        // get text in slide start-end
                        if(slide.children.length > 0){
                            slide.text = data.substr(slide.start + 1, slide.children[0].start - slide.start - 1)
                        }
                        else{
                            slide.text = data.substr(slide.start + 1, slide.end - slide.start -1);
                        }

                        
                        var first_line = slide.text.indexOf("\n");

                        var paras = slide.text.substr(0, first_line).split(";");
                        
                        slide.paras = [];
                        for(var i in paras){
                            if(paras[i].trim().length > 0){
                                var para = paras[i].trim().split("=");
                                slide.paras.push({name: para[0], value: para[1]});
                            }
                        }

                        slide.html = md_con.makeHtml(slide.text.substr(first_line));

                        if(slide.parent){
                            slide.parent.children.push(slide);
                            slide = slide.parent;

                            if(slide.parent){
                                parent = slide.parent;
                            }else{
                                parent = null;
                            }
                        }else{
                            slides.push(slide);
                            slide = null;
                        }
                    }

                    if(tag == "\""){
                        inString = !inString;
                    }
                }

                return slides;
            }

            function append_slides($div, slides){
                for(var i in slides){
                    $slide = $("<div class='step'>");

                    $slide.html(slides[i].html);

                    for(var j in slides[i].paras){
                        $slide.attr("data-"+slides[i].paras[j].name, 
                            slides[i].paras[j].value)
                    }

                    $div.append($slide);

                    if(slides[i].children.length > 0){
                        append_slides($slide, slides[i].children)
                    }
                }
            }

            function append($container, data){
                var slides = get_slides(data);

                return append_slides($container, slides);
            }
        });
    };

})( jQuery );