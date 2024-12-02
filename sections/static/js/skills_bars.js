document.addEventListener("DOMContentLoaded", () => {
            const progressBars = document.querySelectorAll(".progress-bar");
            progressBars.forEach((bar) => {
                const width = bar.style.width;
                bar.style.width = "0";
                setTimeout(() => {
                    bar.style.width = width;
                }, 100);
            });
        });