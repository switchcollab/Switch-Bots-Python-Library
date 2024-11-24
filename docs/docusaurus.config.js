// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

const organizationName = "switchcollab";
const projectName = "Switch-Bots-Python-Library";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Swibots',
  tagline: 'Switch Python Library for bots and apps!',
  url: `https://${organizationName}.github.io`,
  baseUrl: `/${projectName}/`,
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: organizationName, // Usually your GitHub org/user name.
  projectName: projectName, // Usually your repo name.

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        theme: {
          customCss: [
            require.resolve('./src/css/custom.css'),
          ],
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'SwiBots',
        logo: {
          alt: 'SwiBots Site Logo',
          src: 'img/switch-logo.png',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Docs',
          },
          // { to: '/blog', label: 'Blog', position: 'left' },
          {
            href: 'https://github.com/switchcollab/Switch-Bots-Python-Library',
            label: 'GitHub',
            position: 'right',
          },
          {
            href: "https://pypi.org/project/swibots",
            label: "PyPi",
            "position": "right"
          }
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Docs',
                to: '/docs/intro',
              },
            ],
          },
         {
             title: 'Community',
            items: [
               {
                 label: 'Switch',
               href: 'https://switch.click/c/support',
               },
               {
                 label: 'Twitter',
                 href: 'https:/x.com/switch_pe',
               },
             ],
           },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/switchcollab/Switch-Bots-Python-Library',
              },
              {
                label: "PyPi",
                href: "https://pypi.org/project/swibots/"
              }
            ],
          },
        ],
//        copyright: `Copyright © ${new Date().getFullYear()} Switch. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
      algolia: {
        appId: 'TTGB3VL9CC',

        apiKey: '3fa9ddccaad65348dfc0a7a7fcaf95eb',

        indexName: 'switchcollabio',

        // Optional: see doc section below
        contextualSearch: true,

        // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
//        externalUrlRegex: 'external\\.com|domain\\.com',

        // Optional: Replace parts of the item URLs from Algolia. Useful when using the same search index for multiple deployments using a different baseUrl. You can use regexp or string in the `from` param. For example: localhost:3000 vs myCompany.com/docs
  //      replaceSearchResultPathname: {
    //      from: '/docs/', // or as RegExp: /\/docs\//
      //    to: '/',
       // },

        // Optional: Algolia search parameters
        searchParameters: {},

        // Optional: path for search page that enabled by default (`false` to disable it)
        searchPagePath: 'search',

        // Optional: whether the insights feature is enabled or not on Docsearch (`false` by default)
        insights: true
      }
    }),

  headTags: [
    {
      tagName: 'meta',
      attributes: {
        name: 'google-site-verification',
        content: 'yC1cNX1v5yzD_O87LDsebxnxy7KTEoe4-WE3OTQ6q80'
      }
    }
  ],
};

module.exports = config;
