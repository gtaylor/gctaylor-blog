export const SITE = {
  website: "https://gctaylor.com/",
  author: "Greg Taylor",
  profile: "https://www.linkedin.com/in/gregtaylorcu/",
  desc: "A minimal, responsive and SEO-friendly Astro blog theme.",
  title: "Greg Taylor",
  ogImage: "astropaper-og.jpg",
  lightAndDarkMode: true,
  postPerIndex: 4,
  postPerPage: 25,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: true,
  showBackButton: true, // show back button in post detail
  editPost: {
    enabled: false,
    text: "Edit page",
    url: "https://github.com/gtaylor/gctaylor-blog/edit/main/",
  },
  dynamicOgImage: true,
  dir: "ltr", // "rtl" | "auto"
  lang: "en", // html lang code. Set this empty and default will be "en"
  timezone: "America/Los_Angeles", // Default global timezone (IANA format) https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
} as const;
