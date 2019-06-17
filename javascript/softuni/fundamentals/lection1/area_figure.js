function calcArea(w, h, W, H) {
    let [s1, s2, s3] = [w*h, W*H, Math.min(h, H) * Math.min(w, W)];
    return s1 + s2 - s3;
}