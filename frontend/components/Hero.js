export const Hero = () => {
    return (
        <>
        <div className="relative top-12 mt-12 p-12 flex flex-col justify-center items-center gap-8 h-full w-full">
            <h1 className="mb-8 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"><mark className="px-2 text-white bg-blue-600 rounded-xl dark:bg-blue-500">Brand</mark>AI</h1>
            <h2 className="mb-4 text-2xl font-bold leading-none tracking-tight text-gray-900 md:text-3xl lg:text-4xl dark:text-white"><span className="underline underline-offset-3 decoration-8 decoration-blue-400 dark:decoration-blue-600">Your agent for Brand Positioning</span></h2>
            <p className="mb-6 w-[70%] text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">Unlock your brand's potential with Agentic Workflow: where strategic insights meet dynamic execution. Elevate your positioning through a seamless blend of creativity and data-driven decisions, empowering your brand to resonate authentically in the market. Transform your vision into impact, ensuring every step aligns with your unique narrative and audience engagement.</p>
            <a href="#" className="inline-flex items-center justify-center px-5 py-3 text-base font-medium text-center text-white rounded-xl bg-gradient-to-br from-purple-600 to-blue-500 group-hover:from-purple-600 group-hover:to-blue-500 hover:text-white dark:text-white focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800">
                Learn more
                <svg className="w-3.5 h-3.5 ms-2 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
            </svg>
            </a>
        </div>
        </>
    )
}