import card
import deck
import character
import area
import single_use
import hermit
import win_conditions
import specials

from constants import Alleg, CardType

# elements.py
# Encodes all characters, win conditions, special abilities,
# game areas, decks, and cards in an element factory. Every
# game context is initialized with its own element factory.


class ElementFactory:
    """Make all elements needed for the game."""

    def __init__(self):

        # Initialize white cards
        white_cards = [
            card.Card(
                title="神秘罗盘",
                desc="移动时，你可以掷两次骰子，并选择其中一次结果。",
                color=CardType.White,
                holder=None,
                is_equip=True,
                use=None
            ),
            card.Card(
                title="护身符",
                desc="你不会受到黑卡「嗜血蜘蛛」「吸血蝙蝠」或「炸药」造成的伤害。",
                color=CardType.White,
                holder=None,
                is_equip=True,
                use=None
            ),
            card.Card(
                title="幸运胸针",
                desc="你不会受到区域「怪异森林」造成的伤害，但仍然可以被它治疗。",
                color=CardType.White,
                holder=None,
                is_equip=True,
                use=None
            ),
            card.Card(
                title="银色念珠",
                desc="如果你杀死另一名角色，你可以拿走其所有装备卡。",
                color=CardType.White,
                holder=None,
                is_equip=True,
                use=None
            ),
            card.Card(
                title="朗基努斯之枪",
                desc="如果你是已经公开身份的猎人，并且你的攻击成功，则额外造成 2 点伤害。",
                color=CardType.White,
                holder=None,
                is_equip=True,
                use=None
            ),
            card.Card(
                title="降临",
                desc="如果你是猎人，你可以公开身份。公开身份后，或者你已经公开身份时，你可以完全恢复伤害。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.advent
            ),
            card.Card(
                title="破魔镜",
                desc="如果你是暗影（Unknown 除外），你必须公开身份。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.disenchant_mirror
            ),
            card.Card(
                title="祝福",
                desc="选择一名除你之外的角色并掷六面骰。该角色恢复等同于骰子点数的伤害。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.blessing
            ),
            card.Card(
                title="巧克力",
                desc="如果你是 Allie、Agnes、Emi、Ellen、Unknown 或 Ultra Soul，你可以公开身份。公开身份后，或者你已经公开身份时，你可以完全恢复伤害。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.chocolate
            ),
            card.Card(
                title="隐藏知识",
                desc="本回合结束后，再次轮到你的回合。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.concealed_knowledge
            ),
            card.Card(
                title="守护天使",
                desc="直到你的下一个回合开始，你不会受到其他角色直接攻击造成的伤害。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.guardian_angel
            ),
            card.Card(
                title="圣袍",
                desc="你的攻击少造成 1 点伤害，并且你受到的攻击伤害减少 1 点。",
                color=CardType.White,
                holder=None,
                is_equip=True,
                use=lambda is_attack, successful, amt: max(
                    0, amt - 1)  # applies to both attack and defend
            ),
            card.Card(
                title="审判之火",
                desc="除你之外的所有角色受到 2 点伤害。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.judgement
            ),
            card.Card(
                title="急救",
                desc="将一名角色的伤害值设为 7（可以选择自己）。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.first_aid
            ),
            card.Card(
                title="治疗圣水",
                desc="恢复 2 点伤害。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.holy_water
            ),
            card.Card(
                title="治疗圣水",
                desc="恢复 2 点伤害。",
                color=CardType.White,
                holder=None,
                is_equip=False,
                use=single_use.holy_water
            )
        ]

        # Initialize black cards
        black_cards = [
            card.Card(
                title="诅咒之剑·正宗",
                desc=(
                    "You must attack another character on your turn."
                    " This attack uses the 4-sided die."),
                color=CardType.Black,
                holder=None,
                is_equip=True,
                use=None
            ),
            card.Card(
                title="机枪",
                desc=(
                    "Your attack will affect all characters in your"
                    " attack range (the dice are rolled only once)."),
                color=CardType.Black,
                holder=None,
                is_equip=True,
                use=None
            ),
            card.Card(
                title="手枪",
                desc="除你自己的范围外，所有范围都变成你的攻击范围。",
                color=CardType.Black,
                holder=None,
                is_equip=True,
                use=None
            ),
            card.Card(
                title="屠夫刀",
                desc="如果你的攻击成功，则额外造成 1 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=True,
                use=lambda is_attack, successful, amt: amt +
                1 if (is_attack and successful) else amt
            ),
            card.Card(
                title="电锯",
                desc="如果你的攻击成功，则额外造成 1 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=True,
                use=lambda is_attack, successful, amt: amt +
                1 if (is_attack and successful) else amt
            ),
            card.Card(
                title="生锈的宽刃斧",
                desc="如果你的攻击成功，则额外造成 1 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=True,
                use=lambda is_attack, successful, amt: amt +
                1 if (is_attack and successful) else amt
            ),
            card.Card(
                title="喜怒无常的哥布林",
                desc="从任意一名角色那里偷取一张装备卡。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.moody_goblin
            ),
            card.Card(
                title="喜怒无常的哥布林",
                desc="从任意一名角色那里偷取一张装备卡。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.moody_goblin
            ),
            card.Card(
                title="嗜血蜘蛛",
                desc="对任意一名角色造成 2 点伤害，同时自己受到 2 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.bloodthirsty_spider
            ),
            card.Card(
                title="吸血蝙蝠",
                desc="对任意一名角色造成 2 点伤害，同时恢复自己的 1 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.vampire_bat
            ),
            card.Card(
                title="吸血蝙蝠",
                desc="对任意一名角色造成 2 点伤害，同时恢复自己的 1 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.vampire_bat
            ),
            card.Card(
                title="吸血蝙蝠",
                desc="对任意一名角色造成 2 点伤害，同时恢复自己的 1 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.vampire_bat
            ),
            card.Card(
                title="恶魔仪式",
                desc="如果你是暗影，可以公开身份。公开身份后，你可以完全恢复伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.diabolic_ritual
            ),
            card.Card(
                title="香蕉皮",
                desc="将你的一张装备卡交给另一名角色。如果你没有装备卡，则受到 1 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.banana_peel
            ),
            card.Card(
                title="炸药",
                desc="掷两颗骰子，对位于骰子总点数所对应区域的所有角色造成 3 点伤害（如果掷出 7，则什么也不会发生）。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.dynamite
            ),
            card.Card(
                title="灵魂人偶",
                desc="选择一名角色并掷六面骰。如果点数为 1 至 4，则对该角色造成 3 点伤害；如果点数为 5 或 6，则你受到 3 点伤害。",
                color=CardType.Black,
                holder=None,
                is_equip=False,
                use=single_use.spiritual_doll
            )
        ]

        # Initialize hermit cards
        hermit_cards = [
            card.Card(
                title="隐士的勒索",
                desc="我猜你是中立者或猎人。如果是，你必须给当前玩家一张装备卡，或者受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.blackmail
            ),
            card.Card(
                title="隐士的勒索",
                desc="我猜你是中立者或猎人。如果是，你必须给当前玩家一张装备卡，或者受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.blackmail
            ),
            card.Card(
                title="隐士的贪婪",
                desc="我猜你是中立者或暗影。如果是，你必须给当前玩家一张装备卡，或者受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.greed
            ),
            card.Card(
                title="隐士的贪婪",
                desc="我猜你是中立者或暗影。如果是，你必须给当前玩家一张装备卡，或者受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.greed
            ),
            card.Card(
                title="隐士的愤怒",
                desc="我猜你是猎人或暗影。如果是，你必须给当前玩家一张装备卡，或者受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.anger
            ),
            card.Card(
                title="隐士的愤怒",
                desc="我猜你是猎人或暗影。如果是，你必须给当前玩家一张装备卡，或者受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.anger
            ),
            card.Card(
                title="隐士的耳光",
                desc="我猜你是猎人。如果是，你受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.slap
            ),
            card.Card(
                title="隐士的耳光",
                desc="我猜你是猎人。如果是，你受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.slap
            ),
            card.Card(
                title="隐士的法术",
                desc="我猜你是暗影。如果是，你受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.spell
            ),
            card.Card(
                title="隐士的驱魔",
                desc="我猜你是暗影。如果是，你受到 2 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.exorcism
            ),
            card.Card(
                title="隐士的抚慰",
                desc="我猜你是中立者。如果是，你恢复 1 点伤害！（但是，如果你没有伤害，则受到 1 点伤害！）",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.nurturance
            ),
            card.Card(
                title="隐士的援助",
                desc="我猜你是猎人。如果是，你恢复 1 点伤害！（但是，如果你没有伤害，则受到 1 点伤害！）",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.aid
            ),
            card.Card(
                title="隐士的聚集",
                desc="我猜你是暗影。如果是，你恢复 1 点伤害！（但是，如果你没有伤害，则受到 1 点伤害！）",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.huddle
            ),
            card.Card(
                title="隐士的教诲",
                desc="我猜你最大生命值为 12 或以上。如果是，你受到 2 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.lesson
            ),
            card.Card(
                title="隐士的霸凌",
                desc="我猜你最大生命值为 11 或以下。如果是，你受到 1 点伤害！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.bully
            ),
            card.Card(
                title="隐士的预言",
                desc="你必须将自己的角色信息秘密地展示给当前玩家！",
                color=CardType.Hermit,
                holder=None,
                is_equip=False,
                use=hermit.prediction
            )
        ]

        # Initialize white, black, hermit decks
        self.WHITE_DECK = deck.Deck(cards=white_cards)
        self.BLACK_DECK = deck.Deck(cards=black_cards)
        self.HERMIT_DECK = deck.Deck(cards=hermit_cards)

        # Initialize characters

        self.CHARACTERS = [
            character.Character(
                name="女武神",
                alleg=Alleg.Shadow,
                max_damage=13,
                win_cond=win_conditions.shadow,
                win_cond_desc="所有猎人（或者 3 名中立者）都已死亡。",
                special=specials.valkyrie,
                special_desc="攻击时，你只能掷四面骰，并造成骰子点数对应的伤害。",
                resource_id="valkyrie"
            ),
            character.Character(
                name="吸血鬼",
                alleg=Alleg.Shadow,
                max_damage=13,
                win_cond=win_conditions.shadow,
                win_cond_desc="所有猎人（或者 3 名中立者）都已死亡。",
                special=specials.vampire,
                special_desc="如果你攻击一名玩家并造成伤害，你可以恢复自己的 2 点伤害。",
                resource_id="vampire"
            ),
            character.Character(
                name="狼人",
                alleg=Alleg.Shadow,
                max_damage=14,
                win_cond=win_conditions.shadow,
                win_cond_desc="所有猎人（或者 3 名中立者）都已死亡。",
                special=specials.werewolf,
                special_desc="受到攻击后，你可以立即进行反击。",
                resource_id="werewolf"
            ),
            character.Character(
                name="超灵魂",
                alleg=Alleg.Shadow,
                max_damage=11,
                win_cond=win_conditions.shadow,
                win_cond_desc="所有猎人（或者 3 名中立者）都已死亡。",
                special=specials.ultra_soul,
                special_desc="你的回合开始时，你可以对位于冥界之门的一名玩家造成 3 点伤害。",
                resource_id="ultra-soul"
            ),
            character.Character(
                name="艾莉",
                alleg=Alleg.Neutral,
                max_damage=8,
                win_cond=win_conditions.allie,
                win_cond_desc="游戏结束时你仍然存活。",
                special=specials.allie,
                special_desc="每局游戏一次，你可以将自己的伤害完全恢复。",
                resource_id="allie"
            ),
            character.Character(
                name="鲍勃",
                alleg=Alleg.Neutral,
                max_damage=10,
                win_cond=win_conditions.bob,
                win_cond_desc="你拥有至少 5 张装备卡。",
                special=specials.bob,
                special_desc="如果你的攻击造成至少 2 点伤害，你可以从目标玩家那里偷取一张装备卡，而不是造成伤害。",
                resource_id="bob1",
                modifiers={'min_players': 4, 'max_players': 6}
            ),
            character.Character(
                name="鲍勃",
                alleg=Alleg.Neutral,
                max_damage=10,
                win_cond=win_conditions.bob,
                win_cond_desc="你拥有至少 5 张装备卡。",
                special=specials.bob,
                special_desc="如果你杀死另一名玩家，你可以拿走其所有装备卡。",
                resource_id="bob2",
                modifiers={'min_players': 7, 'max_players': 8}
            ),
            character.Character(
                name="凯瑟琳",
                alleg=Alleg.Neutral,
                max_damage=11,
                win_cond=win_conditions.catherine,
                win_cond_desc="你要么是第一个死亡的玩家，要么是最后两名存活玩家之一。",
                special=specials.catherine,
                special_desc="你的回合开始时，你恢复 1 点伤害。",
                resource_id="catherine"
            ),
            character.Character(
                name="乔治",
                alleg=Alleg.Hunter,
                max_damage=14,
                win_cond=win_conditions.hunter,
                win_cond_desc="所有暗影都已死亡。",
                special=specials.george,
                special_desc="每局游戏一次，在你的回合开始时，你可以选择一名玩家，并对其造成四面骰投出的点数对应的伤害。",
                resource_id="george"
            ),
            character.Character(
                name="风香",
                alleg=Alleg.Hunter,
                max_damage=12,
                win_cond=win_conditions.hunter,
                win_cond_desc="所有暗影都已死亡。",
                special=specials.fuka,
                special_desc="每局游戏一次，在你的回合开始时，你可以将任意一名玩家的伤害值设为 7。",
                resource_id="fu-ka"
            ),
            character.Character(
                name="富兰克林",
                alleg=Alleg.Hunter,
                max_damage=12,
                win_cond=win_conditions.hunter,
                win_cond_desc="所有暗影都已死亡。",
                special=specials.franklin,
                special_desc="每局游戏一次，在你的回合开始时，你可以选择一名玩家，并对其造成六面骰投出的点数对应的伤害。",
                resource_id="franklin"
            ),
            character.Character(
                name="艾伦",
                alleg=Alleg.Hunter,
                max_damage=10,
                win_cond=win_conditions.hunter,
                win_cond_desc="所有暗影都已死亡。",
                special=specials.ellen,
                special_desc="每局游戏一次，在你的回合开始时，你可以选择一名玩家，并永久使其特殊能力失效。",
                resource_id="ellen"
            )
        ]

        # Initialize areas
        self.AREAS = [
            area.Area(
                name="隐士小屋",
                desc="抽取一张隐士卡。",
                domain=[2, 3],
                action=lambda gc, player: player.drawCard(gc.hermit_cards),
                resource_id="hermits-cabin"
            ),
            area.Area(
                name="冥界之门",
                desc="从你选择的牌堆中抽取一张卡。",
                domain=[4, 5],
                action=area.underworld_gate_action,
                resource_id="underworld-gate"
            ),
            area.Area(
                name="教堂",
                desc="抽取一张白卡。",
                domain=[6],
                action=lambda gc, player: player.drawCard(gc.white_cards),
                resource_id="church"
            ),
            area.Area(
                name="墓地",
                desc="抽取一张黑卡。",
                domain=[8],
                action=lambda gc, player: player.drawCard(gc.black_cards),
                resource_id="cemetery"
            ),
            area.Area(
                name="怪异森林",
                desc="恢复 1 点伤害，或对任意一名玩家造成 2 点伤害。",
                domain=[9],
                action=area.weird_woods_action,
                resource_id="weird-woods"
            ),
            area.Area(
                name="古老祭坛",
                desc="从任意一名玩家那里偷取一张装备卡。",
                domain=[10],
                action=area.erstwhile_altar_action,
                resource_id="erstwhile-altar"
            )
        ]
