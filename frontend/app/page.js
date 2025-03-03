import { Navbar } from "@/components/Navbar";
import { Hero } from "@/components/Hero";
import { Chat } from "@/components/Chat";
import { Footer } from "@/components/Footer";
import { Toaster } from "react-hot-toast";

export default function Home() {
  return (
    <>
      <Navbar/>
      <Hero/>
      <Chat/>
      <Footer/>
      <Toaster/>
    </>
  );
}
