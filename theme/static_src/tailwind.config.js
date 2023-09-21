/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../templates/**/*.html",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {
      gridTemplateRows: {
        16: "repeat(16, minmax(0, 1fr))",
        24: "repeat(24, minmax(0, 1fr))",
        26: "repeat(26, minmax(0, 1fr))",
        38: "repeat(38, minmax(0, 1fr))",
        74: "repeat(74, minmax(0, 1fr))",
      },
      gridRow: {
        'span-8': 'span 8 / span 8',
        'span-9': 'span 9 / span 9',
        'span-10': 'span 10 / span 10',
        'span-11': 'span 11 / span 11',
        'span-16': 'span 16 / span 16',
      },
      gridRowStart: {
        '7': '7',
        '8': '8',
        '9': '9',
      },
      colors: {
        'custom-black': '#0a0a0b',
        'gray-border': '#212427',
        'gray-bg': '#121212',
        'gray-bg-hover': '#1a1a1a',
        'gray-text': '#9c9c9c',
        'gray-text-light': '#525252',
        'custom-purple': '#772af4'
      },
      "animation": {
        "background-shine": "background-shine 2s linear infinite",
        "text-gradient": "text-gradient 1.5s linear infinite",
        "border-width": "border-width 3s infinite alternate",
        marquee: 'marquee 15s linear infinite',
        marquee2: 'marquee2 15s linear infinite',
        spin: 'spin 15s linear infinite',
      },
      "keyframes": {
        "background-shine": {
          "from": {
            "backgroundPosition": "0 0"
          },
          "to": {
            "backgroundPosition": "-200% 0"
          }
        },
        "text-gradient": {
          "to": {
            "backgroundPosition": "200% center"
          }
        },
        "border-width": {
          "from": {
            "width": "10px",
            "opacity": "0"
          },
          "to": {
            "width": "200px",
            "opacity": "1"
          }
        },
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-100%)' },
        },
        marquee2: {
          '0%': { transform: 'translateX(100%)' },
          '100%': { transform: 'translateX(0%)' },
        },
        spin: {
          "to": {
            transform: 'rotate(360deg)'
          }
        }
      }
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
  ],
};