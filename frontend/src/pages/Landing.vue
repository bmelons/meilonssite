<template>
  <div class="box content">
    <h2 style="font-size: 30pt;" >About me!</h2>
    <p><b style="font-size: 20pt;">Hi, im Neil/Meilon!</b>  <img src="https://64.media.tumblr.com/e0b68275ed1cc54682ff2e1ed1c08368/a150b8283b99824b-97/s100x200/8a1588604fbd9aff8c433eedaa6b5f0796e61167.pnj" style="height: 20px; width: 30px;"><br/>
      Welcome to my website ^w^ <br/>
      I'm a furry artist that does other creative stuff on the side!
      This website is a place where you can<br/>
      My fursona's name is pronounced "may-lawn" <audio src="/speech.mp3?url" type="audio/mpeg"></audio>
    
    </p>
      <ul>
        <li>Get a commission quote automatically </li>
        <li>Browse my character reference sheets</li>
        <li>Find all of my socials</li>
        <li>more eventually... 🤫</li>
      </ul>
      <br/>
      <p>
      I hope you find something here useful or entertaining!! :3c
      </p>
      <img src="/NYA!~.png?url" style="margin: 2em;">
      <div class="blinkies">
        <span v-for="blinky in blinkies"> <img :src="blinky"> </span>
      </div>
  </div>
</template>

<style>

blinkies{
  margin: 1em;
  display: flex;
  flex-wrap:wrap;
  justify-content: center;
  max-width: 200px;
}

img {
  width: 200px;
}

p {
  justify-content: left;
}

ul {
  font-size: large;
  list-style-type:circle;
}


</style>
<script lang="ts">
const blinkyurls : string[] = [
  'https://adriansblinkiecollection.neocities.org/b8.gif',
  "https://adriansblinkiecollection.neocities.org/b51.gif",
  "https://adriansblinkiecollection.neocities.org/b40.gif",
  "https://adriansblinkiecollection.neocities.org/c61.gif",
  "https://adriansblinkiecollection.neocities.org/d31.gif",
  "https://adriansblinkiecollection.neocities.org/d35.gif",
  "https://adriansblinkiecollection.neocities.org/e3.gif",
  "https://adriansblinkiecollection.neocities.org/e48.gif",
  "https://adriansblinkiecollection.neocities.org/v14.gif",
  "https://adriansblinkiecollection.neocities.org/v20.gif",
  "https://adriansblinkiecollection.neocities.org/v26.gif",
  "https://adriansblinkiecollection.neocities.org/v71.gif",
  "https://adriansblinkiecollection.neocities.org/f10.gif",
  "https://adriansblinkiecollection.neocities.org/g35.gif",
  "https://adriansblinkiecollection.neocities.org/g99.gif",
  "https://adriansblinkiecollection.neocities.org/19.gif"


]
export default {
  data() {
    return {
      blinkies: blinkyurls
    }
  }
}
</script>

