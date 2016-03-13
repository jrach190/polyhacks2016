function Sock(x, y) {
    this.x = x;
    this.y = y;
}

var c, ctx, socks, sky, waves, boat, width, height, bx, by, dx, count, rot, drot, sink;


$(document).ready(function () {
    dx = 0;
    sink = false;
    drot = 0;
    rot = 0;
    count = 0;
    c = document.getElementById("can");
    ctx = c.getContext("2d");
    width = window.innerWidth;
    height = window.innerHeight;

    bx = width / 2 - 200;
    socks = [];

    sky = document.getElementById("sky");
    waves = document.getElementById("waves");
    boat = document.getElementById("boat");
    sock = document.getElementById("sock");

    TweenLite.selector = jQuery;



    $(document).click(function (e) {
        addSock(e.pageX, e.pageY);
        main();
    });
    var running = true;

    setInterval(main, 1000 / 50);

});


function addSock(x, y) {
    var seck = new Sock(x, 0);
    socks.push(seck);
}

function main() {
    count++;
    if (count > 1500) {
        count = 0;
    }
    tick();

    draw();

}

function tick() {
    drot = 0;
    socks.forEach(function (s, i) {
        s.y += 4;
        console.log("bx: " + bx + "\nmouse x:" + s.x);
        if (s.y > 600 && s.x >= bx && s.x <= bx + 400) {
            if (s.x <= bx + 200) {
                drot -= .3;
                dx +=.1;
            } else {
                drot += .3;
                dx +=.1;
            }
        }
        if (s.y > 800) {
            socks.splice(i, 1);
        }
    });
    if (!sink) {

        if (drot == 0) {
            drot += -rot / 10;
        }
        if (count % 5 == 0) {
            rot += drot;
            bx += dx;
        }
        if(bx >= width - 350){
            dx -= 1;
        }else if( bx <= 0){
            dx += 1;
        }
        var style = {
            left: bx,
            transform: "rotate(" + rot + "deg)"
        };
        $('#boat').css(style);
        console.log(rot);
        if (Math.abs(rot) > 50) {
            sink = true;
        }
    } else {
        var style = {
            top: "+=1"
            , opacity: "-=.002"
        };
        $('#boat').css(style);
    }
}


function draw() {
    by = 750;
    //Sky
    ctx.drawImage(sky, 0, 0, width, height * 3 / 4);


    socks.forEach(function (s) {
        ctx.drawImage(sock, s.x, s.y, 30, 50);
    });
    //Ship and socks
    //drawBoat(0);



    //Sea
    ctx.fillStyle = "#00BBD1";
    ctx.fillRect(0, height * 3 / 4, width, 250);
    //ctx.drawImage(waves, -20, height*3/4 - 100, width+40, 250);
}

function drawBoat(degrees) {

    // save the unrotated context of the canvas so we can restore it later
    // the alternative is to untranslate & unrotate after drawing
    ctx.save();

    // move to the center of the canvas
    ctx.translate(bx, by);

    // rotate the canvas to the specified degrees
    ctx.rotate(degrees * Math.PI / 180);

    // draw the image
    // since the context is rotated, the image will be rotated also
    ctx.drawImage(boat, -boat.width / 2, -boat.height / 2, 500, 250);

    // we’re done with the rotating so restore the unrotated context
    ctx.restore();
}