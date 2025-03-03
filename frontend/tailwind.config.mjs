/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
      animation: {
        typewriter: "typewriter 1s steps(60) forwards",
        blink: "blink 1s infinite"
      },
      keyframes: {
        typewriter: {
          from: { width: "0" },
          to: { width: "100%" }
        },
        blink: {
          from: { "border-right-color": "transparent" },
          to: { "border-right-color": "black" }
        }
      }
    },
  },
  plugins: [],
};