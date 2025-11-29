

<template>
  <div id="app">
    
    <vue-particles
      id="tsparticles"
      @particles-loaded="particlesLoaded"
    />
    <vue-particles class="p" id="tsparticles" @particles-loaded="particlesLoaded" :options="options" />
    
  </div>
</template>

<style lang="css">
.p {
  background-image: linear-gradient(0deg, #9283a5 0%, #a186a2 100%);
  /* background-color: red; */
}

</style>

<script lang="js">
const particlesLoaded = async (container) => {
  console.log('Particles container loaded', container)
}

export default {
  data() {
    return {
      options: {
        background: {
          color: {
            value: '#423b46',
          },
          image : "var(--primary-bg-gradient)"
        },
        fpsLimit: 144,
        interactivity: {
          events: {
            onClick: {
              enable: false,
              mode: 'push',
            },
            onHover: {
              enable: true,
              mode: 'push',
            },
          },
          modes: {
            bubble: {
              distance: 400,
              duration: 2,
              opacity: 0.8,
              size: 40,
            },
            push: {
              quantity: 40,
            },
            repulse: {
              distance: 50,
              duration: .1,
            },
          },
        },
        particles: {
          color: {
            value: '#ffffff',
          },
          links: {
            enable: false,
          },
          move: {
            direction: 'bottom',
            enable: true,
            outModes: 'out',
            random: false,
            speed: 1,
            straight: false,
          },
          number: {
            density: {
              enable: true,
            },
            value: 350,
          },
          opacity: {
            value: 0.2,
          },
          shape: {
            type: 'circle',
          },
          size: {
            value: { min: 1, max: 5 },
          },
        },
        detectRetina: true,
      },
    }
  },
}
</script>