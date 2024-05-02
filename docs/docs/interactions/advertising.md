---
sidebar_position: 3
---
# Advertising

## Earn Revenue with Switch Mini-Apps
- Via Advertising from Switch Mini-Apps, app developers get an opportunity to earn and make their income.

## How to apply for Ads Program?
1. Find and open Monetize bot on Switch from apps section.
2. On first open, It will ask you to apply for approval.
3. Fill the basic required details, wait for approval.

We provide responses within 24 hours, If, for your application it take long, ping us at [Support Chat](https://iswitch.click/support)

## Integrating Bot to display Ads.

### Types of Ad
Currently, We support 2 types of Ads.
1. `VIDEO_1`: display one ad.
2. `VIDEO_2`: display two ads, one after other.

Bot Developer can choose this according to there wish and place of integration.

### Preparing Bot to handle ads.
- Ads can be displayed any callback request.

Let's go step by step.
### AdButton
1. AdButton provide a different animation, which differs other button from Ad Buttons.

We created a page, where 
```python
from swibots import AdButton

@client.on_callback_query(regexp("page"))
async def __e(ctx: BotContext[CallbackQueryEvent]):
    # We added 2 ad buttons
    # ad_1 for type 1
    # ad_2 for type 2
    # in Next step, we add callbacks to callback data.
    page = AppPage(
            components=[
                Text("Click below button to open ad."),
                AdButton("Watch Ad [1]", callback_data="ad_1"),
                AdButton("Watch Ad [2]", callback_data="ad_2"),
            ]
        )
    await ctx.event.answer(
        callback=page
    )
```

### Callbacks
We created the callback handlers, which 

- We define a `success_callback`, which is a callback data, which is triggered after user watch the ads successfully.

```python
@client.on_callback_query(regexp("ad_1"))
async def e(ctx: BotContext[CallbackQueryEvent]):
    print(ctx)
    await ctx.event.show_ad(
        ad_type="VIDEO_1",
        id="9195dwda-jnfafWasl-fflsle2",
        success_callback="Success"
        
    )

@client.on_callback_query(regexp("ad_2"))
async def __e(ctx: BotContext[CallbackQueryEvent]):
    print(ctx)
    await ctx.event.show_ad(
        ad_type="VIDEO_2",
        id="e452-sjgmamsmf-fjnsndl-kk7af",
        success_callback="Success"
    )
```

### Handling watched event.
- We defined the success_callback in previous step, we can perform any action when the user watched the ad completely.

```python
@client.on_callback_query(regexp("Success"))
async def __e(ctx: BotContext[CallbackQueryEvent]):
    await ctx.event.answer("Showed", show_alert=True)
```

[Check the Complete Code Sample](#)